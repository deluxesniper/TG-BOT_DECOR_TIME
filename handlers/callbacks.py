from gc import callbacks

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from Keyboard.inline import info_company, info_stor,fact_again,paint_to_calculate
from Keyboard.reply import under_the_menu,my_advertisement
from services.gpt_random_fact import get_fact
from services.json import save_advertisement
from stor.contacts import XL_city, XL_email, XL_phone,XL_opening_hours,XL_address
from services.variable import save_message
class AdvertisementStates(StatesGroup):
    waiting_for_text = State()
from handlers.states import Calcs_adhesive, Calcs_granella, Calcs_kraft_pro_matt, Calcs_Durata, Create_Users_messages

router = Router()

@router.callback_query(F.data=="Raschet")
async def paint_to_calculate_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Вы хотите рассчитать количество не обходимой объёма краски, лака или грунтовки, тогда выберите нужную",reply_markup=paint_to_calculate())


@router.callback_query(F.data=="adhesive")
async def calculate_Priming_Adhesive_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_adhesive.waiting)
    await call.answer()

@ router.message(Calcs_adhesive.waiting)
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

            await message.answer(
                f"С вашей площадью {granella} м²\n"
                f"Вам потребуется: {result:.2f} литров штукатурки Granella\n"
                f"Расход: {granella_consumption} м²/литр"
            )
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

            await message.answer(
                f"С вашей площадью {kraft_pro_matt} м²\n"
                f"Вам потребуется: {result:.2f} литров  лака Kraft pro matt\n"
                f"Расход: {kraft_pro_matt_consumption} м²/литр"
            )
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

            await message.answer(
                f"С вашей площадью {durata} м²\n"
                f"Вам потребуется: {result:.2f} литров  лака Durata\n"
                f"Расход: {durata_consumption} м²/литр"
            )
            await state.clear()



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



@router.callback_query(F.data =="random_fact")
async def random_handler(call:CallbackQuery):
    await call.answer('Щас расскажу как появились краски, каждая история отличается от другой',show_alert=True)
    fact = await get_fact()
    await call.message.answer(f'Факт: {fact}',reply_markup=fact_again())



@router.message(F.text == "Объявления")
async def menu_handler(message: Message):
    await message.answer("Что хотите сделать: создать или просмотреть ваши объявления",reply_markup=under_the_menu())



@router.message(F.text =="Создать Объявление")
async def zagolovok(message: Message,state: FSMContext):
    await state.set_state(Create_Users_messages.user_for_text)
    await state.update_data(zagalovok=message.text)
    await message.answer( "Отлично! Давайте создадим объявление.\n\n"
        "📌 Шаг 1 из 6: Введите заголовок объявления:",)




@router.message(Create_Users_messages.user_for_text,F.text)
async def create_user_handler(message: Message,state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Create_Users_messages.name)
    await message.answer("📝 Шаг 2 из 6: напишите ваше имя:" )


@router.message(Create_Users_messages.name,F.text)
async def create_name_handler(message: Message,state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Create_Users_messages.age)
    await  message.answer("📝Шаг 3 из 6: напишите ваш возраст ")



@router.message(Create_Users_messages.age,F.text)
async def create_age_handler(message: Message,state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Create_Users_messages.city)
    await  message.answer("📝Шаг 4 из 6: напишите ваш город ")


@router.message(Create_Users_messages.city,F.text)
async def create_city_handler(message: Message,state: FSMContext):
    await state.update_data(announcement=message.text)
    await state.set_state(Create_Users_messages.announcement)
    await message.answer("📝Шаг 5 из 6: напишите текст объявления")




@router.message(Create_Users_messages.announcement,F.text)
async def create_payment_handler(message: Message,state: FSMContext):
    await state.update_data(payment=message.text)
    await state.set_state(Create_Users_messages.payment)
    await message.answer("📝Шаг 6 из 6: напишите вашу цену")


@router.message(Create_Users_messages.payment,F.text)
async def create_Send_messages_handler(message: Message,state: FSMContext):
    data= await state.get_data()
    my_advertisement={
         "user_id": message.from_user.id,
        "username": message.from_user.username,
        "zagolovok":data["zagalovok"],
        "name": data['name'],
        "age": data['age'],
        "city": data['city'],
        "announcement": data['announcement'],
        "payment": data['payment'],
    }
    save_message(my_advertisement)
    await state.clear()

    ad_text=f"""

    ✅ Объявление
    успешно
    создано!

    Заголовок: {my_advertisement['zagolovok']}
    Имя: {my_advertisement['name']}
    Возраст: {my_advertisement['age']}
    Город: {my_advertisement['city']}
    Описание: {my_advertisement['announcement']}
    Цена: {my_advertisement['payment']}
    

    Объявление
    сохранено
    в
    базе!
    """
    await message.answer(ad_text)


@router.message(F.photo)
async def photo(message:Message):
    await message.answer(f"Я получил от вас фотографию")
img = FSInputFile('media/img')



@router.message(F.voice)
async def voice(message:Message):
    await message.answer(f" Вы отправили Голосовое сообщение")

