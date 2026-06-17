import datetime
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models import Base


class Task(BaseModel):
    id: UUID
    title: str
    user_id: int


class TaskModel(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
