from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.models import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False, unique=True)

    tasks = relationship('TaskModel', back_populates='user')
