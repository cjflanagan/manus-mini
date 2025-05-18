import json
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

try:
    import openai
except ImportError:  # pragma: no cover - openai not installed
    openai = None

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")


def perform_openai_chat(messages, functions=None, model="gpt-3.5-turbo"):
    if not openai:
        return {"error": "openai package not available"}
    openai.api_key = OPENAI_API_KEY
    kwargs = {"model": model, "messages": messages}
    if functions:
        kwargs["functions"] = functions
    response = openai.ChatCompletion.create(**kwargs)
    return response["choices"][0]["message"]


def do_web_search(query: str):
    resp = requests.get(
        "https://duckduckgo.com", params={"q": query, "format": "json"}
    )
    return resp.json()


def do_reddit_search(query: str):
    resp = requests.get(
        "https://www.reddit.com/search.json", params={"q": query}, headers={"User-Agent": "chat-app"}
    )
    return resp.json()


def do_wiki_search(query: str):
    resp = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "opensearch",
            "search": query,
            "limit": 5,
            "namespace": 0,
            "format": "json",
        },
    )
    return resp.json()


@csrf_exempt
def chat_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)
    data = json.loads(request.body.decode())
    messages = data.get("messages", [])
    model = data.get("model", "gpt-3.5-turbo")
    functions = [
        {
            "name": "web_search",
            "description": "Search the web",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
        {
            "name": "reddit_search",
            "description": "Search Reddit posts",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
        {
            "name": "wiki_search",
            "description": "Search Wikipedia",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    ]
    result = perform_openai_chat(messages, functions=functions, model=model)
    return JsonResponse(result, safe=False)


@csrf_exempt
def web_search(request):
    query = request.GET.get("q", "")
    return JsonResponse(do_web_search(query), safe=False)


@csrf_exempt
def reddit_search(request):
    query = request.GET.get("q", "")
    return JsonResponse(do_reddit_search(query), safe=False)


@csrf_exempt
def wiki_search(request):
    query = request.GET.get("q", "")
    return JsonResponse(do_wiki_search(query), safe=False)
