from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

url_youtube = 'https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4'

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='btn1')],
    [KeyboardButton(text='btn2'), KeyboardButton(text='btn3')],
], resize_keyboard=True, input_field_placeholder="Тут текст")

main_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VIDEO', url=url_youtube)]
])

test_list = [
    'fire', 'water', 'air', 'earth'
]


async def inline_test_list():
    keyboard = InlineKeyboardBuilder()
    for el in test_list:
        keyboard.add(InlineKeyboardButton(text=el, url='https://www.youtube.com/'))
    return keyboard.adjust(3).as_markup()
