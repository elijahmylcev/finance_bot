import asyncio
from datetime import datetime
from aiogram import executor
from handlers import dp
import threading
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency
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
#             currency text
#           )
#           """)
# c.execute("""
#           CREATE TABLE income (
#             date text,
#             category text,
#             sum integer,
#             currency text
#           )
#           """)


# db.close()

# async def infinity() -> None:
#   while True:
#     gold_pay = get_k_currency()
#     print(gold_pay)
#     cash = get_cash_currency()
#     print(cash)
    
#     try:
#       db = sqlite3.connect('bot_data.db')
#       c = db.cursor()
#       print("Подключен к SQLite")

#       sqlite_insert_with_param = """INSERT INTO currency
#                             (date, cash_num, gold_num)
#                             VALUES (?, ?, ?);"""

#       data_tuple = (datetime.now(), cash, gold_pay)
#       c.execute(sqlite_insert_with_param, data_tuple)
#       db.commit()
#       print("Success")
#       c.close()
#     except sqlite3.Error as error:
#       print("Ошибка при работе с SQLite", error)
#     finally:
#       if db:
#         db.close()
#         print("Соединение с SQLite закрыто")
#     await asyncio.sleep(120)
  

async def on_startup(dp) -> None:
  import filters
  filters.setup((dp))

  from utils.notify_admins import on_startup_notify
  await on_startup_notify(dp)

  from utils.set_bot_commands import set_default_commands
  await set_default_commands(dp)
  print('Bot запущен')
  

if __name__ == '__main__':
  # loop = asyncio.get_event_loop()
  # loop.create_task(infinity())
  # thread = threading.Thread(target=infinity)
  # thread.start()
  executor.start_polling(dp, on_startup=on_startup)
  