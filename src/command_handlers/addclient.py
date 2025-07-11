from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile, InputMediaDocument, Message

from utils import run_wireguard_cmd

__all__ = ["router"]

router = Router()


class AddClientState(StatesGroup):
    name = State()


@router.message(Command("addclient"))
async def addclient(message: Message, state: FSMContext) -> None:
    await state.set_state(AddClientState.name)
    await message.answer("Enter client name")


@router.message(AddClientState.name)
async def process_added_clientname(message: Message, state: FSMContext) -> None:
    await state.clear()
    client_name = message.text.strip()
    run_wireguard_cmd(["--addclient", client_name])

    conf_path = Path.home() / f"{client_name}.conf"
    png_path = Path.home() / f"{client_name}.png"

    conf_file = FSInputFile(conf_path, filename=f"{client_name}.conf")
    png_file = FSInputFile(png_path, filename=f"{client_name}.png")

    media = [
        InputMediaDocument(media=conf_file, caption=f"{client_name}`s config"),
        InputMediaDocument(media=png_file, caption=f"{client_name}`s QR-code"),
    ]

    await message.answer_media_group(media)
