from gc import callbacks
from services.dialogs import PERSONS
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



####$$НАчало inlane menu



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
        ],
            [
                InlineKeyboardButton(text="Рекоминдации по фильмам",callback_data="Recommendations"),
                InlineKeyboardButton(text="Переводчик",callback_data='language'),
            ]

        ]

    keyboard=InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard



####$$конец inlane menu



####$$НАчало menu  для рассчета красок



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


####$$Конец menu  для рассчета красок


####$$НАчало menu  про магазины


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



def get_persons_keyboard():
    kb_list=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=name,callback_data=f'select_persons:{name}')]
        for name in PERSONS
    ]
    )
    return kb_list

def close():
    kb_list=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Закончить',callback_data='close')
        ]
    ])
    return kb_list



def topic_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='История', callback_data='topic:history')],
            [InlineKeyboardButton(text='Наука', callback_data='topic:science')],
            [InlineKeyboardButton(text='IT', callback_data='topic:it')],
        ]
    )
    return kb

def quiz_answers():
    Kb_List = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Еще вопрос', callback_data='next_question')],
            [InlineKeyboardButton(text='Сменить тему', callback_data='change_topic')],
            [InlineKeyboardButton(text='Закончить', callback_data='end_quiz')],
        ]
    )
    return Kb_List


def movie_menu():
    kb_list=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Ужасы', callback_data='films:horror')],
            [InlineKeyboardButton(text='Комедия', callback_data='films:comedy')],
            [InlineKeyboardButton(text='Боевик', callback_data='films:action')],
        ]
    )
    return kb_list

def recommendation_move():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Не нравится', callback_data='dislike_recommendation')],
            [InlineKeyboardButton(text='Сменить жанр', callback_data='change_genre')],
            [InlineKeyboardButton(text='Закончить', callback_data='end_recommendations')],
        ]
    )
    return kb