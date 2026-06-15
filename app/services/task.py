import logging
import uuid

from app.models.task import Task
from app.services.exceptions import InvalidTaskNumberException, TaskNotFoundException

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str, user_id: int) -> Task:
        current = Task(
            id=uuid.uuid7(),
            title=title,
            user_id=user_id
        )

        self._tasks.append(current)
        logger.debug("Added task %s", current)
        logger.debug("Current count of tasks: %s", len(self._tasks))

        return current

    def get_tasks(self, user_id: int) -> list[Task]:
        return [task for task in self._tasks if task.user_id == user_id]

    def remove_task(self, user_id: int, task_number: int) -> Task:
        if task_number <= 0:
            raise InvalidTaskNumberException

        user_tasks = [task for task in self._tasks if task.user_id == user_id]

        if task_number > len(user_tasks):
            raise TaskNotFoundException

        task = user_tasks[task_number - 1]
        logger.debug("Removed task %s", task)

        self._tasks.remove(task)

        return task
