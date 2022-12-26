from loader import dp
from datetime import datetime, date, time
from aiogram import types
from aiogram.utils.markdown import hcode, hbold

import sqlite3

@dp.message_handler(text='Курс ₮(USDT)')
async def command_currency(message: types.Message) -> None:
  
  try:
    db = sqlite3.connect('bot_data.db')
    c = db.cursor()
    SQLite_select = 'SELECT * FROM currency_usdt WHERE date=(SELECT MAX(date) FROM currency_usdt);'

    c.execute(SQLite_select)
    data = c.fetchall()
    print(data)
    date_src = datetime.strptime(data[0][0], "%Y-%m-%d %H:%M:%S.%f")
    if date_src.date() == datetime.now().date():
      date_str = f'Зафиксировано сегодня в {date_src.time()}'
    else:
      date_str = f'Дата: {date_src.date()}, Время фиксации курса: {date_src.time()}'
    usdt = data[0][1]
    percent = data[0][2]
    c.close()
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
  finally:
    if db:
      db.close()
  await message.answer(f'{hbold(date_str)}\n\n\n<b>Курс ₮: {hcode(str(usdt) + "₽")} \nИзменился на: {hcode(str(percent) + "%")}</b>')
  