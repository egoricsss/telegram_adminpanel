from aiogram import Router
from aiogram.filters import Command, and_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils import IsAdmin, run_wireguard_cmd, GetClientNameState

router = Router()


@router.message(and_f(IsAdmin(), Command("removeclient")))
async def removeclient(message: Message, state: FSMContext) -> None:
    await state.set_state(GetClientNameState.name)
    await message.answer("Enter client name to delete")


@router.message(GetClientNameState.name)
async def process_removed_clientname(message: Message, state: FSMContext) -> None:
    await state.clear()
    client_name = message.text.strip()
    wireguard_response = run_wireguard_cmd(["--removeclient", client_name])
    await message.answer(f"<code>{wireguard_response}</code>")
