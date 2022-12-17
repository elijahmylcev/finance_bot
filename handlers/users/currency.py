from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency
from threading import Thread
from states import currency_tenge

@dp.message_handler(text='Курс тенге')
async def command_currency(message: types.Message, state: FSMContext):
  # korona_pay = Thread(target=get_k_currency)
  # cash = Thread(target=get_cash_currency)
  # cash.start()
  # korona_pay.start()
  # cash.join()
  # korona_pay.join()
  korona_val = get_k_currency()
  cash_val = get_cash_currency()
  await message.answer(f'Курс на золотой короне: {korona_val}₸ \nКурс в обменниках: {cash_val}₸')
