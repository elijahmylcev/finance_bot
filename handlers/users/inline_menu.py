from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.inline import ikb_menu
import sqlite3
from loader import dp

@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
  await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Курс ₸')
async def send_message(call: CallbackQuery):
  action = call.data
  if action == 'Курс ₸':
    try:
      db = sqlite3.connect('bot_data.db')
      c = db.cursor()
      print("Подключен к SQLite")

      SQLite_select = 'SELECT * FROM currency WHERE date=(SELECT MAX(date) FROM currency);'

      c.execute(SQLite_select)
      data = c.fetchall()
      c.close()
    except sqlite3.Error as error:
      print("Ошибка при работе с SQLite", error)
    finally:
      if db:
        db.close()
        print("Соединение с SQLite закрыто")
  await call.answer(f'Time: {data[0][0]}\nКурс ₽ на золотой короне: {data[0][2]}₸ \nКурс ₽ в обменниках: {data[0][1]}₸')
