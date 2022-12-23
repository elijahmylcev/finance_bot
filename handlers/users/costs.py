from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

from states import costs

@dp.message_handler(Command(['costs', 'Записать расходы']))
async def category_(message: types.Message):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

  mark_category = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'Аренда жилья'),
        KeyboardButton(text=f'Комунальные услуги'),
      ],
      [
        KeyboardButton(text=f'Еженедельная закупка'),
        KeyboardButton(text=f'Покупка на неделе'),
      ]
    ],
    resize_keyboard=True
  )

  await message.answer(f'Запишем расходы \nВыбери категорию.', reply_markup=mark_category)
  await costs.category.set()


@dp.message_handler(state=costs.category)
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
  
  await message.answer(f'Категория {answer}, сколько деньжат потратели?',
                       reply_markup=nums_key)
  await costs.count.set()

@dp.message_handler(state=costs.count)
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
  await costs.currency.set()
  
@dp.message_handler(state=costs.currency)
async def state2(message: types.Message, state: FSMContext):
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
  
  await message.answer(f'Валюта: {answer}, Кто закупился?',
                       reply_markup=executor_key)
  await costs.executor.set()

@dp.message_handler(state=costs.executor)
async def state3(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(executor=answer)
  data = await state.get_data()
  category = data.get('category')
  count = data.get('count')
  currency = data.get('currency')
  executor = data.get('executor')
  await message.answer(f'Записали \nВалюта: {currency}. \nСумма: {count} \nКатегория: {category} \n Исполнитель {executor}', reply_markup=kb_menu)

  await state.finish()
  
@dp.message_handler(text='Записать расходы')
async def category_(message: types.Message):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

  mark_category = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'Аренда жилья'),
        KeyboardButton(text=f'Комунальные услуги'),
      ],
      [
        KeyboardButton(text=f'Еженедельная закупка'),
        KeyboardButton(text=f'Покупка на неделе'),
      ]
    ],
    resize_keyboard=True
  )

  await message.answer(f'Запишем расходы \nВыбери категорию.', reply_markup=mark_category)
  await costs.category.set()


@dp.message_handler(state=costs.category)
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
  
  await message.answer(f'Категория {answer}, сколько деньжат потратели?',
                       reply_markup=nums_key)
  await costs.count.set()

@dp.message_handler(state=costs.count)
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
  await costs.currency.set()
  
@dp.message_handler(state=costs.currency)
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
  
  await message.answer(f'Валюта: {answer}, Кто закупился?',
                       reply_markup=executor_key)
  await costs.executor.set()

@dp.message_handler(state=costs.executor)
async def state4(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(executor=answer)
  data = await state.get_data()
  category = data.get('category')
  count = data.get('count')
  currency = data.get('currency')
  executor = data.get('executor')
  await message.answer(f'Записали \nВалюта: {currency}. \nСумма: {count} \nКатегория: {category} \nИсполнитель {executor}', reply_markup=kb_menu)

  await state.finish()
  