from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'XXX'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(text = ['Urban', 'ff'])
async def urban_message(message):
    #print('Urban message')
    await message.answer('Urban message')

@dp.message_handler(commands = ['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):                 # Любые сообщения(без ключевых слов)
    #print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
