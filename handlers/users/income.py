from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

from states import income

@dp.message_handler(Command('income'))
async def category_(message: types.Message):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

  mark_category = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'Зарплата'),
        KeyboardButton(text=f'Личный заказ'),
        KeyboardButton(text=f'Фриланс'),
        KeyboardButton(text=f'Премия'),
      ],
    ],
    resize_keyboard=True
  )

  await message.answer(f'Запишем доход \nВыбери категорию.', reply_markup=mark_category)
  await income.category.set()


@dp.message_handler(state=income.category)
async def state1(message: types.Message, state: FSMContext):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(category=answer)
  
  nums_key = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'1'),
        KeyboardButton(text=f'2'),
        KeyboardButton(text=f'3'),
        KeyboardButton(text=f'4'),
        KeyboardButton(text=f'5'),
        KeyboardButton(text=f'6'),
        KeyboardButton(text=f'7'),
        KeyboardButton(text=f'8'),
        KeyboardButton(text=f'9'),
        KeyboardButton(text=f'0'),
      ],
    ],
    resize_keyboard=True
  )
  
  await message.answer(f'Категория {answer}, сколько деньжат?)',
                       reply_markup=nums_key)
  await income.count.set()

@dp.message_handler(state=income.count)
async def state2(message: types.Message, state: FSMContext):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(count=answer)
  
  currency_key = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'₸'),
        KeyboardButton(text=f'₽'),
        KeyboardButton(text=f'$'),
        KeyboardButton(text=f'€'),
        KeyboardButton(text=f'£')
      ],
    ],
    resize_keyboard=True
  )
  
  await message.answer(f'Сумма: {answer}, В какой валюте?',
                       reply_markup=currency_key)
  await income.currency.set()

@dp.message_handler(state=income.currency)
async def state3(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(currency=answer)
  data = await state.get_data()
  category = data.get('category')
  count = data.get('count')
  currency = data.get('currency')
  await message.answer(f'Записали \nВалюта: {currency}. \nСумма: {count} \nКатегория: {category}', reply_markup=kb_menu)

  await state.finish()
