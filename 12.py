from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7346715807:AAGlBVpL6ZvgQ8ZZTvaGlnCMHMAxK08ZEw4'
bot = Bot(token=api)
db = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button1, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@db.message_handler(commands=['start'])
async def start(message):
    await message.answer('Нажмите на кнопку - Рассчитать', reply_markup=kb)


@db.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    await message.answer(f'{data["third"], data["second"], data["first"]}')
    await message.answer(f'Ваша норма калорий -> {10 * float(data["third"]) + 6.25 * float(data["second"]) - 5 * float(data["first"]) + 5}')
    await state.finish()


@db.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@db.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@db.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@db.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb)


@db.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@db.message_handler()
async def tup(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)








