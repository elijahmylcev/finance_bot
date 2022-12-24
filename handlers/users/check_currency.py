from loader import dp
import pandas as pd

import sqlite3

async def check_currency():
  try:
    db = sqlite3.connect('bot_data.db')
    df = pd.read_sql('SELECT * FROM currency ORDER BY date DESC LIMIT 2;', db)
    print(df)
    gold = df['gold_num'].tolist()
    cash = df['cash_num'].tolist()
    if gold[1] - gold[0] == 0:
      await dp.bot.send_message(f'{gold[0]}')
    await dp.bot.send_message(f'{cash[1]}')
    
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
  finally:
    if db:
      db.close()