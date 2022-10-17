from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp

from states import register

@dp.message_handler(Command('register'))
async def register_(message: types.Message):
  await message.answer(f'Привет, {message.from_user.full_name}! \n Ты начал регистрацию. \n Введи свое имя.')
  await register.write_name.set() #Состояние ввода имени

@dp.message_handler(state=register.write_name)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text #Сохраняем ответ пользователя

  await state.update_data(write_name=answer)
  await message.answer(f'{answer}, сколько тебе лет?')
  await register.old.set()


@dp.message_handler(state=register.old)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(old=answer)
  data = await state.get_data()
  name = data.get('write_name')
  years = data.get('old')
  await message.answer(f'Регистрация успешно завершена! \n Твое имя {name}. \n Тебе {years} лет')

  await state.finish()

