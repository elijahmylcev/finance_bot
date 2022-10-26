from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

from states import converter


@dp.message_handler(Command('converter'))
async def register_(message: types.Message):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
  tenge = '₸'
  rub = '₽'

  currency = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'{tenge} ⇝ {rub}'),
        KeyboardButton(text=f'{rub} ⇝ {tenge}')
      ],
    ],
    resize_keyboard=True
  )

  await message.answer(f'Конвертируем... \nВыбери валюту для конвертации.', reply_markup=currency)
  await converter.currency_current.set()


@dp.message_handler(state=converter.currency_current)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(currency_current=answer)
  await message.answer(f'{answer}, сколько конвертируем?')
  await converter.price_input.set()


@dp.message_handler(state=converter.price_input)
async def state2(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(price_input=answer)
  data = await state.get_data()
  currency = data.get('currency_current')
  price = data.get('price_input')
  await message.answer(f'Конвертация успешна совершена \nВалюта: {currency}. \nСумма: {price}',
                       reply_markup=kb_menu)

  await state.finish()
