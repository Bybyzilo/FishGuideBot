import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from routers import routers
from config import TG_TOKEN



'''Инициализация бота и диспетчера'''
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()



async def main() -> None:
    dp.include_routers(*routers)

    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
