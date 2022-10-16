from aiogram import types
from loader import dp

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
  await message.answer(f'Привет {message.from_user.full_name}! \n'
                       f'Ты выбрал: {message.text}')