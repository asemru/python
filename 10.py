from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import sqlite3

connection = sqlite3.connect('timi.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (username)')

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()


def is_included(username):
    check1 = cursor.execute('SELECT * FROM Users WHERE username=?', (username, ))
    if check1.fetchone() is not None:
        return True
    else:
        return False


api = '' #<--- Водите сюда номер вашего бота
bot = Bot(token=api)
bd = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Регистрация')
kb.add(button)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()



@bd.message_handler(commands=['start'])
async def well(message):
    await message.answer('Хотите зарегестрироваться?', reply_markup= kb)


@bd.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer('Введите имя пользователя')
    await RegistrationState.username.set()


@bd.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()


@bd.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@bd.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(data)
    connection.close()
    await state.finish()



@bd.message_handler()
async def start(message):
    await message.answer('Нажмите на кнопку -> /start чтобы начать общение')









if __name__ == '__main__':
    executor.start_polling(bd, skip_updates=True)


