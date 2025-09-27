from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, InlineKeyboardMarkup

from Keyboard.inline import close, quiz_answers
from services.Qwize import check_answer, get_score
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

class QuizStates(StatesGroup):
    choosing_topic = State()
    waiting_answer = State()

class Move(StatesGroup):
   fedback_waiting= State()






@router.message(MessagesPersona.message)
async def messages_persona_handler(message:Message):
    answer=await ask_role_gpt(message.from_user.id,message.text)
    persona = dialogis[message.from_user.id]['persona']
    await message.answer(f'{answer}', reply_markup=close())




@router.message(QuizStates.waiting_answer)
async def waiting_answer_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    question = data.get('question')
    result = await check_answer(question, message.text)
    await message.answer('Сейчас дам ответ')
    if result == 'правильно':
        score = await increase_score(state)
        await message.answer(f'✅ Правильно, твой счет {score}',reply_markup=quiz_answers())
    else:
        score = await get_score(state)
        await message.answer(f'⛔️ Неправильно твой счет {score}', reply_markup=quiz_answers())

