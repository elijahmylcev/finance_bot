import time
import requests
from bs4 import BeautifulSoup
from config import page, user_agent


class Currency:
  page = page
  headers = {'User-agent': user_agent}

  currency_converted_price = 0
  difference = 0.5

  def __init__(self):
    self.currency_converted_price = self.get_currency_price()

  def get_currency_price(self):
    full_page = requests.get(self.page, headers=self.headers)
    soup = BeautifulSoup(full_page.content, 'lxml')

    convert = soup.find_all('div', class_="fl")
    c = convert[2].text
    return float(c)

  def check_currency(self):
    currency = self.get_currency_price()
    if currency > self.currency_converted_price + self.difference:
      print("Курс 〒 вырос")
    elif currency <= self.currency_converted_price - self.difference:
      print("Курс 〒 упал || не изменился")

    print(f'Сейчас курс 〒 : {currency}')
    time.sleep(3)
    self.check_currency()


currency = Currency()


currency.check_currency()
