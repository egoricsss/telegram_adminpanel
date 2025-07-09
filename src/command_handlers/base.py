from aiogram import Router
from aiogram.types import Message

__all__ = ["router"]

router = Router()


@router.message()
async def echo(message: Message) -> None:
    await message.answer(message.text)
