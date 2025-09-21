
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def info_inline():
    kb_list=[
        [InlineKeyboardButton(text='Информация о нас',callback_data='info'),
        InlineKeyboardButton(text="Наш сайт", url='https://decortime.pro/')],
        [InlineKeyboardButton(text="Расчет кол-во Штукатурки, Лака и Грунтовки", callback_data='Raschet')],
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard



def info_company():
    kb_list=[
        [
          InlineKeyboardButton(text="Где мы находимся",callback_data='Locations'),
          InlineKeyboardButton(text="Наши магазины", callback_data='stors')
        ]
    ]
    info_keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return info_keyboard



def formula_racheta():
    kb_list=[
        [InlineKeyboardButton(text="Рассчет штукатурки",callback_data='plaster'),
         InlineKeyboardButton(text="Рассчет лака", callback_data='varnish')
        ],
        [InlineKeyboardButton(text="Рассчет грунтовки",callback_data='primers')]
    ]



def info_stor():
    kb_list=[
        [InlineKeyboardButton(text="Галерея интерьеров «Твинстор",callback_data='Twinstor')]

    ]
    stor_keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return stor_keyboard