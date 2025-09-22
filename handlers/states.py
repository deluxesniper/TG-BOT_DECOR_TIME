from aiogram.fsm.state import State, StatesGroup


class Users(StatesGroup):
    name = State()
    age = State()
    city = State()
    announcement =State()