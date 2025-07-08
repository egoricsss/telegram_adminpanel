from aiogram import Router
from aiogram.filters import Command, and_f
from aiogram.types import Message
from wireguard import run_wireguard_cmd
from utils.filter import IsEgoric

__all__ = ["router"]


router = Router()


@router.message(and_f(IsEgoric(), Command("listclients")))
async def list_clients(message: Message):
    wireguard_response = run_wireguard_cmd(["--listclients"])
    await message.answer(f"List of clients:\n```{wireguard_response}\n```")
