from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = 'NNN'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup): # Создание класса состояний
    UserState = State()
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton( text = 'Рассчитать')
button_2 = KeyboardButton( text = 'Информация')
kb.row(button_1, button_2)                  # Кнопки идут в ряд

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я - бот, помогающий твоему здоровью.', reply_markup = kb)

kb_inline = InlineKeyboardMarkup()          # Инлайн кнопки
but_inline_1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
but_inline_2 = InlineKeyboardButton(text = 'Формулы расчёта' , callback_data = 'formulas')
kb_inline.add(but_inline_1, but_inline_2)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb_inline)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Формулa 10 * ВЕС + 6.25 * РОСТ - 5 * ВОЗРАСТ - 161  - женская')
    await call.answer()

@dp.callback_query_handler(text = 'calories')   # Хэндлер для команды 'Рассчитать'
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)                        # Хэндлер для состояния UserState.age
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)                     # Хэндлер для состояния UserState.growth
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)                     # Хэндлер для состояния UserState.weight
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:                                               # Проверяем тип входных данных (целые числа)
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
        bmr = 10 * weight + 6.25 * growth - 5 * age - 161   # # Упрощённая формула Миффлина - Сан Жеора (женская версия)
        await message.answer(f"Ваша норма калорий: {bmr:.2f} ккал.")
    except ValueError:
        await message.answer("Подходят только числовые значения.")
    await state.finish()            # Финишируем машину состояний

@dp.message_handler()
async def all_message(message):  # Реакция на любые сообщения(без ключевых слов)
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":                          # ------------------------ MAIN ---------------------
    executor.start_polling(dp, skip_updates=True)
