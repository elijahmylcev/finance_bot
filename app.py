import asyncio
from data.config import admins
import logging

from datetime import datetime
from aiogram import executor, Dispatcher
from handlers import dp, check_currency
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency
from functions.get_USDT import get_usdt

import sqlite3

# db = sqlite3.connect('bot_data.db')

# c = db.cursor()

# c.execute("""
#           CREATE TABLE currency (
#             date text,
#             cash_num integer,
#             gold_num integer
#           )
#           """)

# db.close()

# db = sqlite3.connect('bot_data.db')

# c = db.cursor()

# c.execute("""
#           CREATE TABLE costs (
#             date text,
#             category text,
#             cost integer,
#             currency text,
#               executor text

#           )
#           """)
# c.execute("""
#           CREATE TABLE income (
#             date text,
#             category text,
#             sum integer,
#             currency text,
#               executor text

#           )
#           """)

# c.execute("""
#           CREATE TABLE currency_usdt (
#             date text,
#             usdt_rub integer,
#             percent integer
#           )
#           """)


# db.close()



async def infinity(dp: Dispatcher) -> None:
  while True:
    gold_pay = await get_k_currency()
    cash = await get_cash_currency()
    usdt = get_usdt()
    
    try:
      db = sqlite3.connect('bot_data.db')
      c = db.cursor()

      sqlite_insert_with_param = """INSERT INTO currency
                            (date, cash_num, gold_num)
                            VALUES (?, ?, ?);"""

      data_tuple_tenge = (datetime.now(), cash, gold_pay)
      c.execute(sqlite_insert_with_param, data_tuple_tenge)
      
      query_insert_usdt = """
        INSERT INTO currency_usdt
        (date, usdt_rub, percent)
        VALUES (?, ?, ?);
      """
      data_tuple_usdt = (datetime.now(), usdt['price'], usdt['percent'])
      print(data_tuple_usdt)
      c.execute(query_insert_usdt, data_tuple_usdt)
      db.commit()
      print("Success")
      c.close()
      
      check = await check_currency()
      
      for admin in admins:
        try:
          await dp.bot.send_message(chat_id=admin, text=check)
        except Exception as err:
          logging.exception(err)
    except sqlite3.Error as error:
      print("Ошибка при работе с SQLite", error)
    finally:
      if db:
        db.close()
        print("Соединение с SQLite закрыто")
    await asyncio.sleep(900)

async def on_startup(dp) -> None:
  import filters
  filters.setup((dp))

  from utils.notify_admins import on_startup_notify
  await on_startup_notify(dp)

  from utils.set_bot_commands import set_default_commands
  await set_default_commands(dp)
  
  print('Bot запущен')
  

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.create_task(infinity(dp))
  executor.start_polling(dp, on_startup=on_startup)
  