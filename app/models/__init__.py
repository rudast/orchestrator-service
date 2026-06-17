from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import UserModel
from app.models.task import TaskModel

__all__ = ["Base", "UserModel", "TaskModel"]
