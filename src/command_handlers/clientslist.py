from aiogram import Router
from aiogram.filters import Command, and_f
from aiogram.types import Message

from utils import IsAdmin
from utils.wireguard import run_wireguard_cmd

__all__ = ["router"]


router = Router()


@router.message(and_f(IsAdmin(), Command("listclients")))
async def list_clients(message: Message) -> None:
    wireguard_response = run_wireguard_cmd(["--listclients"])
    await message.answer(f"List of clients:\n<code>{wireguard_response}\n</code>")
