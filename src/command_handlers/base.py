from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

__all__ = ["router"]

router = Router()


@router.message(Command("cancel"))
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Cancelled.", reply_markup=ReplyKeyboardRemove())


@router.message()
async def echo(message: Message) -> None:
    await message.answer(message.text)
