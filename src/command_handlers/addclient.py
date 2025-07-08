from aiogram import Router
from aiogram.filters import Command, and_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from utils import IsAdmin, run_wireguard_cmd

router = Router()


class AddClientState(StatesGroup):
    name = State()


@router.message(and_f(IsAdmin(), Command("addclient")))
async def addclient(message: Message, state: FSMContext) -> None:
    await state.set_state(AddClientState.name)
    await message.answer("Enter client name")


@router.message(AddClientState.name)
async def process_added_clientname(message: Message, state: FSMContext) -> None:
    await state.clear()
    client_name = message.text.strip()
    wireguard_response = run_wireguard_cmd(["--addclient", client_name])
    await message.answer(f"{client_name}`s config:\n<code>{wireguard_response}</code>")
