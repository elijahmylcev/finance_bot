from aiogram import types
from aiogram.types import CallbackQuery
from functions.parser_korona import get_k_currency
from functions.parser_cash import get_cash_currency
from keyboards.inline import ikb_menu

from loader import dp

@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
  await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Курс ₸')
async def send_message(call: CallbackQuery):
  action = call.data
  if action == 'Курс ₸':
    korona_val = get_k_currency()
    cash_val = get_cash_currency()
  await call.answer(f'Курс на золотой короне: {korona_val}₸ \nКурс в обменниках: {cash_val}₸')
