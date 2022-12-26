from loader import dp
import pandas as pd

import sqlite3

def check_currency():
  try:
    db = sqlite3.connect('bot_data.db')
    df = pd.read_sql('SELECT * FROM currency ORDER BY date DESC LIMIT 2;', db)
    print(df)
    gold = df['gold_num'].tolist()
    cash = df['cash_num'].tolist()
    if gold[1] > gold[0]:
      gold = gold[1]
    else:
      gold = None
    if cash[1] > cash[0]:
      cash = cash[1]
    else:
      cash = None
      
    return {
      'gold': gold,
      'cash': cash
    }
    
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLit", error)
  finally:
    if db:
      db.close()