
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7646886894:AAED7i2kF5WPyenxWwSgk2nuDb3TcLTNI0I'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)