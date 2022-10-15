import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# Create Bot
bot = Bot(token=os.getenv('BOT_TOKEN'))

# Create Dispatcher
dp = Dispatcher(bot)

@dp.message_handlers() # Аргумент не передан - все сообщения
async def get_message(message: types.Message):
  chat_id = message.chat.id
  # chat_id = types.Message.chat.id || variant
  text = 'Hello, bro'
  await bot.send_message(chat_id, text)

executor.start_polling(dp)