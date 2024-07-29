from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app_bot.keyboards as kb

router = Router()


class Registr(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, твой ID {message.from_user.id}, Имя - {message.from_user.first_name}',
                         reply_markup=kb.main_inline_kb)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали кнопку помощь!')


@router.message(F.text == 'Как дела?')
async def how_deal(message: Message):
    await message.answer('Norm')


@router.message(F.photo)
async def photo_id(message: Message):
    await message.answer(
        f'ID photo {message.photo[-1].file_id}'
        )


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        'https://www.zastavki.com/pictures/originals/2018Animals___Cats_Large_gray_cat_with_a_surprised_look_123712_.jpg',
        caption='Это котик!')


@router.callback_query(F.data == 'catalog')
async def catalog(calback: CallbackQuery):
    await calback.answer('Выбор кнопки "каталог"', show_alert=True)
    await calback.message.edit_text('Тетсовый привет!', reply_markup=await kb.inline_test_list())


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Registr.name)
    await message.answer('Введите имя!')


@router.message(Registr.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registr.number)
    await message.answer('Введите номер телефона!')


@router.message(Registr.number)
async def reg_three(message:  Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, Ваше имя - {data["name"]} и номер телефона - {data["number"]}')
    state.clear()
