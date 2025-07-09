from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from utils import run_wireguard_cmd

__all__ = ["router"]

router = Router()


class RemoveClientState(StatesGroup):
    name = State()
    accept = State()


@router.message(Command("removeclient"))
async def removeclient(message: Message, state: FSMContext) -> None:
    await state.set_state(RemoveClientState.name)
    await message.answer("Enter client name to delete")


@router.message(RemoveClientState.name)
async def process_removed_clientname(message: Message, state: FSMContext) -> None:
    await state.set_state(RemoveClientState.accept)
    client_name = message.text.strip()
    wireguard_response = run_wireguard_cmd(["--removeclient", client_name])
    await message.answer(f"<code>{wireguard_response}</code>")
