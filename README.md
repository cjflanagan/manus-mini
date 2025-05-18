# manus-mini

This repository provides a minimal web portal that uses a Django backend and a
React-based frontend to chat with different AI models. The backend exposes
endpoints for chatting and for invoking searches on the web, Reddit and
Wikipedia. The frontend is a single page that communicates with the backend via
HTTP.

The backend code lives in the `backend` directory, while the minimal frontend is
in `frontend/index.html`.

## Running the server

1. Install the requirements (Django, DRF, openai and requests).
2. Run migrations with `./manage.py migrate`.
3. Start the server with `./manage.py runserver` and open the `frontend/index.html`
   page in your browser.

