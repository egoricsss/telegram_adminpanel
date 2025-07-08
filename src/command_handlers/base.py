from aiogram import Router
from aiogram.types import Message
from utils import IsAdmin

__all__ = ["router"]

router = Router()


@router.message(IsAdmin())
async def echo(message: Message) -> None:
    await message.answer(message.text)
