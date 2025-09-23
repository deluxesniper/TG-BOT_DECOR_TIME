from gc import callbacks

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from Keyboard.inline import info_company, info_stor,fact_again,paint_to_calculate
from Keyboard.reply import under_the_menu,my_advertisement
from services.gpt_random_fact import get_fact
from stor.contacts import XL_city, XL_email, XL_phone,XL_opening_hours,XL_address

class AdvertisementStates(StatesGroup):
    waiting_for_text = State()
from hanndlers.states import Calcs_adhesive,Calcs_granella,

router = Router()

@router.callback_query(F.data=="Raschet")
async def paint_to_calculate_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Вы хотите рассчитать количество не обходимой объёма краски, лака или грунтовки, тогда выберите нужную",reply_markup=paint_to_calculate())


@router.callback_query(F.data=="adhesive")
async def calculate_plaster_handler(call: CallbackQuery, state: FSMContext):
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
                f"Вам потребуется: {result:.2f} литров грунтовки\n"
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
                f"Вам потребуется: {result:.2f} литров грунтовки\n"
                f"Расход: {granella_consumption} м²/литр"
            )
            await state.clear()



@router.callback_query(F.data=="kraft_pro_matt")
async def calculate_plaster_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_granella.waiting)
    await call.answer()

@router.message(Calcs_granella.waiting)
async def formula_granella(message: Message, state: FSMContext):
            kraft_pro_matt = float(message.text)
            kraft_pro_matt_consumption = 4
            result = kraft_pro_matt / kraft_pro_matt_consumption

            await message.answer(
                f"С вашей площадью {kraft_pro_matt} м²\n"
                f"Вам потребуется: {result:.2f} литров грунтовки\n"
                f"Расход: {kraft_pro_matt} м²/литр"
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
async def under_menu_handler(message: Message):
    await message.answer("Напишите свое объявление и нажмите кнопку отправить",reply_markup=my_advertisement())




@router.message(F.photo)
async def photo(message:Message):
    await message.answer(f"Я получил от вас фотографию")
    img = FSInputFile('media/img')



@router.message(F.voice)
async def voice(message:Message):
    await message.answer(f" Вы отправили Голосовое сообщение")

