import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

token = TOKEN

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello, user!')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали кнопку помощь!')


@dp.message(F.text == 'Как дела?')
async def how_deal(message: Message):
    await message.answer('Norm')


@dp.message(F.photo)
async def photo_id(message: Message):
    await message.answer(
        f'ID photo {message.photo[-1].file_id}'
        )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход из бота')
