import logging

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from app.services import task_service

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
        logger.warning("User id is none")
        return

    task_service.add_task(title=title, user_id=message.from_user.id)
    await message.answer(f"Task added: {title}")


@router.message(Command("tasks"))
async def get_tasks(message: Message) -> None:
    if not message.from_user:
        await message.answer("User is not foung")
        logger.warning("User id is none")
        return

    user_id = message.from_user.id
    tasks = task_service.get_tasks(user_id)

    if not tasks:
        await message.answer("No tasks found")
        return

    task_lines = [
        f"\t- {task.title}"
        for task in tasks
    ]

    text = "Your current tasks:\n\n" + "\n".join(task_lines)

    await message.answer(text)
