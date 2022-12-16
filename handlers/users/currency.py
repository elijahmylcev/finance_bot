from loader import dp
from aiogram import types
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency
from threading import Thread

@dp.message_handler(text='Курс тенге')
async def command_hello(message: types.Message):
  korona_pay = Thread(target=get_k_currency)
  cash = Thread(target=get_cash_currency)
  korona_val = korona_pay.start()
  cash_val = cash.start()
  await message.answer(f'Курс на золотой короне: {korona_val}₸ \nКурс в обменниках: {cash_val}₸')
  