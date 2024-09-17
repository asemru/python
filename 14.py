from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '' #<-- Вставить номер своего телеграмм бота
bot = Bot(token=api)
db = Dispatcher(bot, storage=MemoryStorage())

@db.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')


@db.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
