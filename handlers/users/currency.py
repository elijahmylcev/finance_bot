from loader import dp
from aiogram import types
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency


@dp.message_handler(text='Курс тенге')
async def command_hello(message: types.Message):
  # korona_pay = get_k_currency()
  # cash = get_cash_currency()
  await message.answer(f'Курс на золотой короне: {get_k_currency()} \nКурс в обменниках: {get_cash_currency()}')
  