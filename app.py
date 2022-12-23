import asyncio
from aiogram import executor
from handlers import dp
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

async def infinity() -> None:
  while True:
    gold_pay = get_k_currency()
    print(gold_pay)
    cash = get_cash_currency()
    print(cash)
    db = sqlite3.connect('bot_data.db')

    c = db.cursor()
    print(c)
    str_query = f'INSERT INTO currency VALUES ("CURRENT_TIMESTAMP", {cash}, {gold_pay})'
    c.execute(str_query)
    db.commit()
    db.close()
    print('Hello')
    await asyncio.sleep(120)
  

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
  loop.create_task(infinity())
  executor.start_polling(dp, on_startup=on_startup)
  