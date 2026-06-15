import logging

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from app.services import task_service
from app.services.exceptions import TaskNotFoundException, InvalidTaskNumberException

router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message(Command("task"))
async def create_task(message: Message) -> None:
    if not message.text:
        await message.answer("Write task after command /task")
        logger.warning("Message text is none")
        return

    title = message.text.removeprefix("/task").strip()
    if not title:
        await message.answer("Write title after command /task")
        return

    if not message.from_user:
        await message.answer("User is not found")
        logger.warning("User id is none")
        return

    task_service.add_task(title=title, user_id=message.from_user.id)
    await message.answer(f"Task added: {title}")


@router.message(Command("tasks"))
async def get_tasks(message: Message) -> None:
    if not message.from_user:
        await message.answer("User is not found")
        logger.warning("User id is none")
        return

    user_id = message.from_user.id
    tasks = task_service.get_tasks(user_id)

    if not tasks:
        await message.answer("No tasks found")
        return

    task_lines = [
        f"\t{i + 1}) {task.title}"
        for i, task in enumerate(tasks)
    ]

    text = "Your current tasks:\n\n" + "\n".join(task_lines)

    await message.answer(text)


@router.message(Command("delete_task"))
async def delete_task(message: Message) -> None:
    if not message.from_user:
        await message.answer("User is not found")
        logger.warning("User id is none")
        return

    user_id = message.from_user.id

    if not message.text:
        await message.answer("Use /delete_task {number}")
        logger.warning("Message text is none")
        return

    task_number = message.text.removeprefix("/delete_task").strip()

    if not task_number:
        await message.answer("Use /delete_task {number}")
        logger.warning("Task number is none")
        return

    task_number = task_number.split()[0]

    logger.debug("Current task number: %s", task_number)
    if not str.isdigit(task_number):
        await message.answer("Task number is invalid")
        logger.warning("Task number is invalid")
        return

    task_number = int(task_number)

    try:
        task = task_service.remove_task(user_id, task_number)
        await message.answer(f"Task removed: {task.title}")
        logger.info("Task removed: %s", task.id)
    except TaskNotFoundException:
        await message.answer("Task not found")
        logger.warning("Task not found by user_id: %s", user_id)
    except InvalidTaskNumberException:
        await message.answer("Invalid task number by user_id %s", user_id)
