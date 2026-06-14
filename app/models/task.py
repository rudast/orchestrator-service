from uuid import UUID

from pydantic import BaseModel


class Task(BaseModel):
    id: UUID
    title: str
    user_id: int
