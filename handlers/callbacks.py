from gc import callbacks

from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, FSInputFile, ReplyKeyboardRemove
from Keyboard.inline import info_company, info_stor, fact_again, paint_to_calculate, get_persons_keyboard, \
    topic_keyboard, movie_menu, recommendation_move
from Keyboard.reply import under_the_menu, my_advertisement, save_or_clear
from services.Qwize import get_quiz_question, get_score
from services.dialogs import dialogis, PERSONS
from services.gpt_random_fact import get_fact
from services.recomindations import recommendations_move
from stor.contacts import XL_city, XL_email, XL_phone,XL_opening_hours,XL_address
from services.variable import save_message, load_messages
class AdvertisementStates(StatesGroup):
    waiting_for_text = State()
from handlers.states import Calcs_adhesive, Calcs_granella, Calcs_kraft_pro_matt, Calcs_Durata, Create_Users_messages, \
    MessagesPersona, QuizStates,  Move

router = Router()
###____ КОД для Inlane кeyboards  расчета



@router.callback_query(F.data=="Raschet")
async def paint_to_calculate_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Вы хотите рассчитать количество не обходимой объёма краски, лака или грунтовки, тогда выберите нужную",reply_markup=paint_to_calculate())



@router.callback_query(F.data=="adhesive")
async def calculate_Priming_Adhesive_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_adhesive.waiting)
    await call.answer()



@router.message(Calcs_adhesive.waiting)
async def formula_adhesive(message: Message, state: FSMContext):
            adhesive = float(message.text)
            adhesive_consumption = 7.5
            result = adhesive / adhesive_consumption

            await message.answer(
                f"С вашей площадью {adhesive} м²\n"
                f"Вам потребуется: {result:.2f} литров грунтовки Adhesive\n"
                f"Расход: {adhesive_consumption} м²/литр"
            )
            await state.clear()



@router.callback_query(F.data=="granella")
async def calculate_plaster_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_granella.waiting)
    await call.answer()



@router.message(Calcs_granella.waiting)
async def formula_granella(message: Message, state: FSMContext):
    granella = float(message.text)
    granella_consumption = 4
    result = granella / granella_consumption
    await message.answer(f"С вашей площадью {granella} м²\n Вам потребуется: {result:.2f} литров штукатурки Granella\n Расход: {granella_consumption} м²/литр")
    await state.clear()



@router.callback_query(F.data=="kraft_pro_matt")
async def calculate_varnish_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_kraft_pro_matt.waiting)
    await call.answer()



@router.message(Calcs_kraft_pro_matt.waiting)
async def formula_kraft_pro_matt(message: Message, state: FSMContext):
    kraft_pro_matt = float(message.text)
    kraft_pro_matt_consumption = 10
    result = kraft_pro_matt / kraft_pro_matt_consumption
    await message.answer(f"С вашей площадью {kraft_pro_matt} м²\n Вам потребуется: {result:.2f} литров  лака Kraft pro matt\n Расход: {kraft_pro_matt_consumption} м²/литр")
    await state.clear()



@router.callback_query(F.data=="durata")
async def calculate_varnish_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_Durata.waiting)
    await call.answer()



@router.message(Calcs_Durata.waiting)
async def formula_durata(message: Message, state: FSMContext):
    durata = float(message.text)
    durata_consumption = 10
    result = durata / durata_consumption
    await message.answer(f"С вашей площадью {durata} м²\n Вам потребуется: {result:.2f} литров  лака Durata\n Расход: {durata_consumption} м²/литр")
    await state.clear()



###____ Конец Keybords рассчета



####_____ Начало Keybords stors



@router.callback_query(F.data=="info")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Вы выбрали информацию о нас, выберите что хотите знать",reply_markup=info_company())



@router.callback_query(F.data =="Locations")
async def location(call:CallbackQuery):
    await  call.answer()
    await call.message.answer(f"Наш адрес: {XL_city} {XL_address}\n время работы: {XL_opening_hours}\n телефон: {XL_phone}\n EMAIL@: {XL_email}")



@router.callback_query(F.data =="stors")
async def stors(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Адреса наших магазинов",reply_markup=info_stor())



####_____Конец Keyboards stors



######_______ Начало Keybords фактов



@router.callback_query(F.data =="random_fact")
async def random_handler(call:CallbackQuery):
    await call.answer('Щас расскажу как появились краски, каждая история отличается от другой',show_alert=True)
    fact = await get_fact()
    await call.message.answer(f'Факт: {fact}',reply_markup=fact_again())

######_______ Конец Keyboards Фактов



#######_________ Начало Keyboards replay  advertisements

@router.message(F.text == "Объявления")
async def menu_handler(message: Message):
    await message.answer("Что хотите сделать: создать или просмотреть ваши объявления",reply_markup=under_the_menu())



@router.message(F.text =="Создать Объявление")
async def zagolovok(message: Message,state: FSMContext):
    await state.set_state(Create_Users_messages.user_for_text)
    await message.answer( "Отлично! Давайте создадим объявление.\n\n"
        "📌 Шаг 1 из 6: Введите заголовок объявления:")




@router.message(Create_Users_messages.user_for_text,F.text)
async def create_user_handler(message: Message,state: FSMContext):
    await state.update_data(user_for_text=message.text)
    await state.set_state(Create_Users_messages.name)
    await message.answer("📝 Шаг 2 из 6: напишите ваше имя:" )


@router.message(Create_Users_messages.name,F.text)
async def create_name_handler(message: Message,state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Create_Users_messages.age)
    await  message.answer("📝Шаг 3 из 6: напишите ваш возраст ")



@router.message(Create_Users_messages.age,F.text)
async def create_age_handler(message: Message,state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Create_Users_messages.city)
    await  message.answer("📝Шаг 4 из 6: напишите ваш город ")


@router.message(Create_Users_messages.city,F.text)
async def create_city_handler(message: Message,state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Create_Users_messages.announcement)
    await message.answer("📝Шаг 5 из 6: напишите текст объявления")




@router.message(Create_Users_messages.announcement, F.text)
async def create_announcement_handler(message: Message, state: FSMContext):
    await state.update_data(announcement=message.text)  # ✅
    await state.set_state(Create_Users_messages.payment)
    await message.answer("📝 Шаг 6 из 6: напишите вашу цену")


@router.message(Create_Users_messages.payment, F.text)
async def create_payment_handler(message: Message, state: FSMContext):
    await state.update_data(payment=message.text)
    data = await state.get_data()

    preview_text = (
        "📋 Предпросмотр объявления:\n\n"
        f"📌 Заголовок: {data.get('user_for_text')}\n"
        f"👤 Имя: {data.get('name')}\n"
        f"🎂 Возраст: {data.get('age')}\n"
        f"🏙️ Город: {data.get('city')}\n"
        f"📝 Текст: {data.get('announcement')}\n"
        f"💰 Цена: {data.get('payment',)}\n\n"
        "Выберите действие:"
    )

    await state.set_state(Create_Users_messages.confirmation)
    await message.answer(preview_text, reply_markup=save_or_clear())


@router.message(Create_Users_messages.confirmation, F.text.in_(["Сохранить", "Не сохранять"]))
async def handle_confirmation(message: Message, state: FSMContext):
    if message.text == "Сохранить":
        data = await state.get_data()
        message_data = {
            "user_for_text": data.get('user_for_text', 'Не указано'),
            "name": data.get('name'),
            "age": data.get('age'),
            "city": data.get('city'),
            "announcement": data.get('announcement'),
            "payment": data.get('payment')

        }
        save_message(message_data)
        await message.answer("✅ Объявление успешно сохранено!", reply_markup=under_the_menu())
    else:
        await message.answer("❌ Создание объявления отменено.", reply_markup=under_the_menu())

    await state.clear()


@router.message(Create_Users_messages.confirmation)
async def handle_invalid_confirmation(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите действие с помощью кнопок:", reply_markup=save_or_clear())


@router.message(F.text == "Мои Объявления")
async def show_my_advertisements(message: Message):
    # Загружаем все объявления
    advertisements = load_messages()

    if not advertisements:
        await message.answer("У вас пока нет сохраненных объявлений.", reply_markup=under_the_menu())
        return

    # Показываем все объявления
    for i, ad in enumerate(advertisements, 1):
        ad_text = (
                f"📋 Объявление #{i}\n\n"
                f"📌 Заголовок: {ad.get('user_for_text', 'Не указано')}\n"
                f"👤 Имя: {ad.get('name', 'Не указано')}\n"
                f"🎂 Возраст: {ad.get('age', 'Не указано')}\n"
                f"🏙️ Город: {ad.get('city', 'Не указано')}\n"
                f"📝 Текст объявления: {ad.get('announcement', 'Не указано')}\n"
                f"💰 Цена: {ad.get('payment', 'Не указано')}\n"

        )
        await message.answer(ad_text)

    await message.answer(f"📊 Всего объявлений: {len(advertisements)}", reply_markup=under_the_menu())



#######_________ Конец  Keyboards replay  advertisements _____заметка подучить функции JSON



#######@@@_________ Start Keyboards dialogs



@router.callback_query(F.data=="Dialog")
async def talk_dialog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Диалог с известной личностью",reply_markup=get_persons_keyboard())



@router.callback_query(F.data.startswith('select_persons:'))
async def select_persons_handler(call: CallbackQuery,state: FSMContext):
    select_persons=call.data.split(":")[-1]
    # Инициализируем историю
    dialogis[call.from_user.id] = {
        'persona': PERSONS[select_persons],
        'messages': []
    }
    print(dialogis)
    await call.message.answer(f'Ты выбрал {select_persons}. Можешь пообщаться с ним')
    await state.set_state(MessagesPersona.message)



@router.callback_query(F.data.startswith('close'))
async def close_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()


@router.callback_query(F.data=="Qwize")
async def qwize_handler( call:CallbackQuery):
    await call.message.answer('Выбери тему для квиза', reply_markup=topic_keyboard())
    await call.answer()  # Подтверждаем обработку callback



@router.callback_query(F.data.startswith('topic:'))
async def close_mode_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    topic = call.data.split(':')[-1]
    question = await get_quiz_question(topic)
    await state.update_data(question=question)
    await state.update_data(topic=topic)
    await state.set_state(QuizStates.waiting_answer)
    await call.message.answer(f'Тема: {topic}\n\n{question}\nМожешь ответить на вопрос.')


@router.callback_query(F.data == 'next_question')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    data = await state.get_data()
    topic = data.get('topic')
    question = await get_quiz_question(topic)
    await call.message.answer(f'Продолжаем по теме: {topic}\n\n{question}')
    await state.set_state(QuizStates.waiting_answer)


@router.callback_query(F.data == 'change_topic')
async def next_quiz_question_handler(call: CallbackQuery):
    await call.message.answer('Выбери новую тему', reply_markup=topic_keyboard())


@router.callback_query(F.data == 'end_quiz')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    score = await get_score(state)
    await state.clear()
    await call.message.answer(f'🎬 Квиз завершен! Твйо итоговый счет: {score}')



@router.callback_query(F.data == 'Recommendations')
async def genre_handler( call:CallbackQuery):
    await call.message.answer('Выбери Жанр', reply_markup=movie_menu())
    await call.answer()

@router.callback_query(F.data.startswith('films:'))
async def movie_handler(call: CallbackQuery, state: FSMContext):
    rem = call.data.split(":")[-1]
    await call.answer('Сейчас подскажу 5 лучших фильмов по жанру', show_alert=True)
    films= await recommendations_move(rem)
    await state.update_data(films=films)
    await state.set_state(Move.fedback_waiting)
    await call.message.answer(f'🎬 Рекомендации по жанру "{rem}":\n\n{films}',reply_markup=recommendation_move())


@router.callback_query(F.data == 'dislike_recommendation')
async def dislike_recommendation_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Ищу другие варианты...', show_alert=True)
    data = await state.get_data()
    genre = data.get('films')
    # Генерируем новые рекомендации
    new_recommendations = await recommendations_move(genre)
    await call.message.edit_text(f'🎬 Новые рекомендации по жанру "{genre}":\n\n{new_recommendations}',reply_markup=recommendation_move())


@router.callback_query(F.data == 'change_genre')
async def change_genre_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Выбери новый жанр фильмов', reply_markup=movie_menu())

@router.callback_query(F.data == 'end_recommendations')
async def end_recommendations_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('🎬 Рекомендации завершены! Надеюсь, ты нашел что-то интересное!')
