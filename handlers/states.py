from aiogram.fsm.state import State, StatesGroup


class Create_Users_messages(StatesGroup):
    user_for_text = State()
    name = State()
    age = State()
    city = State()
    announcement =State()
    payment = State()
    confirmation = State()


class Calcs_adhesive(StatesGroup):
    waiting = State()



class Calcs_granella(StatesGroup):
    waiting = State()


class Calcs_kraft_pro_matt(StatesGroup):
    waiting = State()



class Calcs_Durata(StatesGroup):
    waiting = State()