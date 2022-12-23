from loader import dp
from aiogram import types
import sqlite3

@dp.message_handler(text='Курс ₸')
async def command_currency(message: types.Message) -> None:
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
  await message.answer(f'Time: {data[0][0]}\nКурс на золотой короне: {data[0][2]}₸ \nКурс в обменниках: {data[0][1]}₸')
