from sqlalchemy import Column, Integer

from app.models import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True, unique=True)
    tg_id = Column(Integer, primary_key=True)
