from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TaskModel


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(
            self,
            user_id: int,
            title: str
    ) -> TaskModel:
        task = TaskModel(user_id=user_id, title=title)

        self._session.add(task)
        await self._session.flush()

        return task

    async def get_all_by_user_id(
            self,
            user_id: int
    ) -> list[TaskModel]:
        statement = (
            select(TaskModel)
            .where(TaskModel.user_id == user_id)
            .order_by(TaskModel.created_at.desc())
        )

        result = await self._session.execute(statement)
        return list(result.scalars().all())

    async def set_completed(
            self,
            task_id: int,
            user_id: int,
            is_completed: bool = True
    ) -> TaskModel | None:
        statement = (
            select(TaskModel)
            .where(TaskModel.id == task_id,
                   TaskModel.user_id == user_id)
        )

        result = await self._session.execute(statement)
        task = result.scalar_one_or_none()

        if task is None:
            return None

        task.is_completed = is_completed
        await self._session.flush()

        return task
