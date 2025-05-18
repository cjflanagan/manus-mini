from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view),
    path('search/web/', views.web_search),
    path('search/reddit/', views.reddit_search),
    path('search/wiki/', views.wiki_search),
]
