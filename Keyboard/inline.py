from gc import callbacks

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def info_inline():
    kb_list=[
        [InlineKeyboardButton(text='Информация о нас',callback_data='info'),
        InlineKeyboardButton(text="Наш сайт", url='https://decortime.pro/')],
        [InlineKeyboardButton(text="Расчет кол-во Штукатурки, Лака и Грунтовки", callback_data='Raschet')],
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard