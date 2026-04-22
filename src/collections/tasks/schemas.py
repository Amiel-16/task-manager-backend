from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    text: str
    done: bool = False


class TaskUpdate(BaseModel):
    text: str | None = None
    done: bool | None = None


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    text: str
    done: bool
    user_id: int
