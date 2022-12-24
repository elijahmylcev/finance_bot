from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import sqlite3
from datetime import datetime
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
      ],
      [
        KeyboardButton(text=f'$'),
        KeyboardButton(text=f'€'),
        KeyboardButton(text=f'£')
      ]
    ],
    resize_keyboard=True
  )
  
  await message.answer(f'Сумма: {answer}, В какой валюте?',
                       reply_markup=currency_key)
  await income.currency.set()

@dp.message_handler(state=income.currency)
async def state3(message: types.Message, state: FSMContext):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
  
  answer = message.text  # Сохраняем ответ пользователя
  await state.update_data(currency=answer)

  executor_key = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'Илья'),
        KeyboardButton(text=f'Света'),
      ],
      [
        KeyboardButton(text=f'Павел'),
        KeyboardButton(text=f'Тима'),
      ]
    ],
    resize_keyboard=True
  )
  
  await message.answer(f'Валюта: {answer}, Чей доход?',
                       reply_markup=executor_key)
  await income.executor.set()
  
@dp.message_handler(state=income.executor)
async def state4(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(executor=answer)
  data = await state.get_data()
  category = data.get('category')
  count = data.get('count')
  currency = data.get('currency')
  executor = data.get('executor')
  try:
    db = sqlite3.connect('bot_data.db')
    c = db.cursor()
    print("Подключен к SQLite")

    sqlite_insert_with_param = """
      INSERT INTO income
      (date, category, sum, currency, executor)
      VALUES (?, ?, ?, ?, ?);
    """

    data_tuple = (datetime.now(), category, count, currency, executor)
    c.execute(sqlite_insert_with_param, data_tuple)
    db.commit()
    print("Success")
    c.close()
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
  finally:
    if db:
      db.close()
      print("Соединение с SQLite закрыто")
  await message.answer(f'Записали \nВалюта: {currency}. \nСумма: {count} \nКатегория: {category} \nПолучатель: {executor}', reply_markup=kb_menu)

  await state.finish()

@dp.message_handler(text='Записать доходы')
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
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
  
  answer = message.text  # Сохраняем ответ пользователя
  await state.update_data(currency=answer)

  executor_key = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'Илья'),
        KeyboardButton(text=f'Света'),
      ],
      [
        KeyboardButton(text=f'Павел'),
        KeyboardButton(text=f'Тима'),
      ]
    ],
    resize_keyboard=True
  )
  
  await message.answer(f'Валюта: {answer}, Чей доход?',
                       reply_markup=executor_key)
  await income.executor.set()
  
@dp.message_handler(state=income.executor)
async def state4(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(executor=answer)
  data = await state.get_data()
  category = data.get('category')
  count = data.get('count')
  currency = data.get('currency')
  executor = data.get('executor')
  try:
    db = sqlite3.connect('bot_data.db')
    c = db.cursor()
    print("Подключен к SQLite")

    sqlite_insert_with_param = """
      INSERT INTO income
      (date, category, sum, currency, executor)
      VALUES (?, ?, ?, ?, ?);
    """

    data_tuple = (datetime.now(), category, count, currency, executor)
    c.execute(sqlite_insert_with_param, data_tuple)
    db.commit()
    print("Success")
    c.close()
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
  finally:
    if db:
      db.close()
      print("Соединение с SQLite закрыто")
  await message.answer(f'Записали \nВалюта: {currency}. \nСумма: {count} \nКатегория: {category} \nПолучатель: {executor}', reply_markup=kb_menu)

  await state.finish()