from aiogram.fsm.state import State, StatesGroup

__all__ = ["GetClientNameState"]


class GetClientNameState(StatesGroup):
    name = State()
    