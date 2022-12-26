import pandas as pd

import sqlite3

def check_usdt():
  try:
    db = sqlite3.connect('bot_data.db')
    df = pd.read_sql('SELECT * FROM currency_usdt ORDER BY date DESC LIMIT 2;', db)
    usdt = df['usdt_rub'].tolist()
    if usdt[1] < usdt[0]:
      usdt = usdt[1]
    else:
      usdt = None
      
    return {
      'usdt': usdt,
    }
    
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLit", error)
  finally:
    if db:
      db.close()