from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

from states import register

@dp.message_handler(Command('register'))
async def register_(message: types.Message):
  from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

  name = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=f'{message.from_user.first_name}'),
      ],
    ],
    resize_keyboard=True
  )

  await message.answer(f'Ты начал регистрацию. \n Введи свое имя.', reply_markup=name)
  await register.write_name.set() #Состояние ввода имени

@dp.message_handler(state=register.write_name)
async def state1(message: types.Message, state: FSMContext):

  answer = message.text #Сохраняем ответ пользователя

  await state.update_data(write_name=answer)
  await message.answer(f'{answer}, сколько тебе лет?')
  await register.old.set()


@dp.message_handler(state=register.old)
async def state2(message: types.Message, state: FSMContext):
  answer = message.text  # Сохраняем ответ пользователя

  await state.update_data(old=answer)
  data = await state.get_data()
  name = data.get('write_name')
  years = data.get('old')
  await message.answer(f'Регистрация успешно завершена! \n Твое имя {name}. \n Тебе {years} лет', reply_markup=kb_menu)

  await state.finish()

