import logging
import uuid

from app.models.task import Task

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str, user_id: int) -> Task:
        current = Task(
            uuid=uuid.uuid7(),
            title=title,
            user_id=user_id
        )

        self._tasks.append(current)
        logger.debug(f"Added task {current}")
        logger.debug(f"Current count of tasks: {len(self._tasks)}")

        return current
