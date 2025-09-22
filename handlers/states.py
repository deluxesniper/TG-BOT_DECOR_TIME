from aiogram.fsm.state import State, StatesGroup


class Users(StatesGroup):
    user_for_text = State()
    name = State()
    age = State()
    city = State()
    announcement =State()


class Calcs_adhesive(StatesGroup):
    waiting = State()