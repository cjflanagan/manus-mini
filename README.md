# manus-mini

This project contains a very small web chat portal built with a Django backend and
a single page HTML/JavaScript frontend.  The backend exposes endpoints that can
chat with OpenAI models and perform web, Reddit and Wikipedia searches.  The
frontend communicates with these API endpoints over HTTP.

The backend code lives in `backend` while the simple frontend page is
`frontend/index.html`.

## Requirements

All Python dependencies are listed in [`requirements.txt`](requirements.txt).
The application requires Python 3.8+.

## Running the server

1. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the OpenAI key** (needed for chat completion):
   ```bash
   export OPENAI_API_KEY=<your-api-key>
   ```
4. **Apply database migrations**:
   ```bash
   python backend/manage.py migrate
   ```
5. **Start the development server**:
   ```bash
   python backend/manage.py runserver
   ```
   The server runs at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
6. **Open the frontend**: load `frontend/index.html` in your browser.  The page
   will communicate with the backend APIs hosted at `/api/`.

