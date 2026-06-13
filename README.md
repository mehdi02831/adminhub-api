# AdminHub — REST API Backend

A clean REST API for the AdminHub admin dashboard, built with FastAPI and SQLAlchemy.

## Tech Stack
- Python 3
- FastAPI
- SQLAlchemy (ORM)
- SQLite (database)
- Pydantic (validation)
- Uvicorn (server)

## Features
- 👥 Full user CRUD
- 📊 Dashboard stats endpoint
- ✅ Input validation with Pydantic
- 🗄️ SQLite database with SQLAlchemy ORM
- 🌐 CORS configured for Vue.js frontend

## Project Structure
adminhub-api/

├── main.py

├── database.py

├── models/

│   └── user.py

├── schemas/

│   └── user.py

└── routes/

└── users.py

## Run Locally

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic

# Start server
uvicorn main:app --reload
```

API runs on `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/{id} | Get single user |
| POST | /users | Create user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |
| GET | /stats | Get dashboard stats |

## API Docs
Visit `http://localhost:8000/docs` for interactive Swagger UI.
