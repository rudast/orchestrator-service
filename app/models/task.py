from uuid import UUID

from pydantic import BaseModel


class Task(BaseModel):
    uuid: UUID
    title: str
    user_id: int
