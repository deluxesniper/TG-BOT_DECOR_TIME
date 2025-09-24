from gc import callbacks

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def info_inline():
    kb_list=[
        [
            InlineKeyboardButton(text='Информация о нас',callback_data='info'),
            InlineKeyboardButton(text="Наш сайт", url='https://decortime.pro/')
        ],

            [InlineKeyboardButton(text="Расчет кол-во Штукатурки, Лака и Грунтовки", callback_data='Raschet'),
            InlineKeyboardButton(text="Факты о красках", callback_data="random_fact")],
        [
            InlineKeyboardButton(text="Игра|Qwize",callback_data='Qwize'),
            InlineKeyboardButton(text="Диалог с личностью",callback_data='Dialog'),
        ]

        ]

    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard



def paint_to_calculate():
    kb_list=[
        [InlineKeyboardButton(text='Грунт Adhesive ',callback_data='adhesive'),
         InlineKeyboardButton(text='Штукатурка GRANELLA ',callback_data='granella')],
        [
            InlineKeyboardButton(text='Лак КRAFT PRO MATT ', callback_data='kraft_pro_matt'),
            InlineKeyboardButton(text='Лак Durata ', callback_data='durata')
        ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard

def info_company():
    kb_list=[
        [
          InlineKeyboardButton(text="Главный офис",callback_data='Locations'),
          InlineKeyboardButton(text="Наши магазины", callback_data='stors')
        ]
    ]
    info_keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return info_keyboard



def paint_racheta():
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

def fact_again():
    kb_list=[
        [InlineKeyboardButton(text="Еще один факт",callback_data='again_fact')]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard