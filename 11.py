from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *
import sqlite3
#Здесь нету возможности узнать свои калории, так как это новый файл, а программу мне надо догнать быстро,
# поэтому я написал без дополнительных функций)))


connection = sqlite3.connect('bibi.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (title)')
def get_all_product(title1, description1, price1):
    #check_user = cursor.execute('SELECT * FROM Users WHERE id=?', (title1))
    #if check_user.fetchone() is None:
    cursor.execute(f'INSERT INTO Users(title, description, price) VALUES(?, ?, ?)', (f'{title1}', f'{description1}', f'{price1}'))




api = ''
bot = Bot(token=api)
db = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Формула')
button2 = InlineKeyboardButton(text='Расчитать')
button3 = InlineKeyboardButton(text='Купить')
kb.add(button1, button2, button3)

kb2 = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button5 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button6 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb2.add(button4, button5, button6, button7)


#@db.message_handler(commands=['start'])
#async def start2(message):
#    await message.answer('Выберите для себя нужную функцию', reply_markup=kb)




@db.message_handler()
async def get_buying_list(message):
    for i1 in range(1, 5):
        get_all_product(f'Продукт {i1}', f'Описание {i1}', f'Цена {i1 * 100}')
    connection.commit()
    connection.close()
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | Описание: {i} | Цена: {i*100}')
        with open('photo/yu.jpg', 'rb') as img:
            await message.answer_photo(img, '')

    #await message.answer('Какой вам продукт нужен?', reply_markup=kb2)

#@db.callback_query_handler(text='product_buying')
#async def send_confirm_message(call):
#    await call.message.answer('Вы успешно приобрели товар!')
#    await call.answer()


#@db.message_handler()
#async def start(message):
#    await message.answer('Нажмите на кнопку -> /start чтобы начать общение')



if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)

