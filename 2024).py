from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '' #<-- Вставить номер своего телеграмм бота
bot = Bot(token=api)
db = Dispatcher(bot, storage=MemoryStorage())


@db.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')


@db.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью')


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)





