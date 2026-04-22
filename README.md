# Task Manager Backend

FastAPI backend with PostgreSQL, SQLAlchemy, JWT authentication, and Docker.

## Project structure

```text
backend/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── core/
│   │    ├── config.py
│   │    └── security.py
│   ├── auth/
│   │    ├── routes.py
│   │    ├── services.py
│   │    └── schemas.py
│   ├── dependencies/
│   │    └── auth.py
│   └── collections/
│        ├── users/
│        │    ├── models.py
│        │    ├── routes.py
│        │    ├── services.py
│        │    └── schemas.py
│        └── tasks/
│             ├── models.py
│             ├── routes.py
│             ├── service.py
│             └── schemas.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run with Docker

From the `backend` folder:

```bash
docker-compose up --build
```

API will be available at:

- `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

## Main endpoints

- `POST /register` - register a new user
- `POST /login` - login and receive JWT token
- `GET /users/me` - get authenticated user
- `GET /tasks` - list user tasks
- `POST /tasks` - create task
- `PUT /tasks/{task_id}` - update task
- `DELETE /tasks/{task_id}` - delete task

## Auth usage

1. Register a user with `POST /register`.
2. Login with `POST /login` and copy `access_token`.
3. In Swagger UI click **Authorize** and paste:
   - `Bearer <access_token>`
