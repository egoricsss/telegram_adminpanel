from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.wireguard import run_wireguard_cmd

__all__ = ["router"]


router = Router()


@router.message(Command("listclients"))
async def list_clients(message: Message) -> None:
    wireguard_response = run_wireguard_cmd(["--listclients"])
    await message.answer(f"<code>{wireguard_response}\n</code>")
