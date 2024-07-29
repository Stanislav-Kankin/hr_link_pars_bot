import asyncio

from aiogram import Bot, Dispatcher
from app_bot.handlers import router

from config import TOKEN

token = TOKEN

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход из бота')
