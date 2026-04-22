from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local imports
from src.auth.routes import router as auth_router
from src.collections.tasks.routes import router as tasks_router
from src.collections.users.routes import router as users_router
from src.database import Base, engine
# Ensure model metadata is loaded before table creation.
from src.collections.tasks import models as _tasks_models  # noqa: F401
from src.collections.users import models as _users_models  # noqa: F401

app = FastAPI(title="Task Manager Backend")

# Configuration la plus permissive possible
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tasks_router)
