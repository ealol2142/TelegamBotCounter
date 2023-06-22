import text

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


mainKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Посчитать предметы',
                                 callback_data='choiser'),
            InlineKeyboardButton(text='Помощь', callback_data='help'),
        ]
    ]
)

backKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back'),
        ]
    ]
)

reply_keyboard = [
    [KeyboardButton(text='Начать', web_app=WebAppInfo(
        url='https://ealol2142.github.io/'))],
    [KeyboardButton(text='Отмена')]
]

choiceKeys = ReplyKeyboardMarkup(
    keyboard=reply_keyboard,
    resize_keyboard=True,
    input_field_placeholder=text.input_field_placeholder)

surveyKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Правильно', callback_data='like'),
            InlineKeyboardButton(text='Не правильно', callback_data='dislike'),
        ]
    ])

removeKey = ReplyKeyboardRemove()
