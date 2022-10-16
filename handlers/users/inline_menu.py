from aiogram import types
from loader import dp

@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
  await message.answer('Инлайн кнопки ниже', reply_markyp=ikb_menu)