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
    await message.delete()


@router.message(Command("tasks"))
async def get_tasks(message: Message) -> None:
    if not message.from_user:
        logger.warning("User id is none")
        return

    user_id = message.from_user.id
    tasks = task_service.get_tasks(user_id)

    if not len(tasks):
        await message.answer("No tasks found")
        return

    text = "Your current tasks:\n\n"
    for task in tasks:
        text += f"\t - {task.title}\n"

    await message.answer(text)
    await message.delete()
