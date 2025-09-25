from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from services.dialogs import ask_role_gpt, dialogis



router=Router()

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

class MessagesPersona(StatesGroup):
    message = State()


@router.message(MessagesPersona.message)
async def messages_persona_handler(message:Message):
    answer=await ask_role_gpt(message.from_user.id,message.text)
    persona = dialogis[message.from_user.id]['persona']
    await message.answer(f'{answer} отвечает ')