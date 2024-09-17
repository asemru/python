from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '' #<-- Вставить номер своего телеграмм бота
bot = Bot(token=api)
db = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


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



@db.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)