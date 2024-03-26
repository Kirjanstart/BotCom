from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


plan = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Сайт/Инст',
            url='https://afanasevaproject.com/inst'
        )
    ]
])


plan_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='YouTube',
            url='https://www.youtube.com/@vkusniy_biz '
        )
    ]
])