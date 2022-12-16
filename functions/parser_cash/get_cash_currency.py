from datetime import datetime
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from .config import page, driver_path
from .get_data import get_data


def get_cash_currency():
  get_data(page_url=page, d_path=driver_path)
  with open('index.html', 'r', encoding="utf-8") as file:
    src = file.read()
  
  soup = BeautifulSoup(src, 'lxml')

  punkt_open_list = soup.find_all('tr', class_='punkt-open')
  objects = []
  for el in punkt_open_list:
    if el.find('span', class_='kurs-warning') == None:
      name = el.find('a', class_='tab').text
      address = el.find('address').text
      time_update = el.find('div', class_='relativeTime').text
      rate = float(el.find('span', {'title': 'RUB - покупка'}).text)
      phone = el.find('a', class_='phone').text
      el_object = {
        'name': name,
        'address': address,
        'time_update': time_update,
        'rate': rate,
        'phone': phone,
      }

      objects.append(el_object)

  df = pd.DataFrame(objects)

  max_rate = max(df['rate'])

  df_max = df[df['rate'] == max_rate]
  mean = df['rate'].mean()
  if not mean or mean == None:
    return 'Что-то пошло не так:('
  else:
    return mean
    
