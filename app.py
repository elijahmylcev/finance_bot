import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

load_dotenv(find_dotenv())
# Create Bot
token = os.getenv('BOT_TOKEN')
bot = Bot(token)

# Create Dispatcher
dp = Dispatcher(bot)
# Аргумент не передан - все сообщения
@dp.message_handler()
async def get_message(message: types.Message):
  chat_id = message.chat.id
  # chat_id = types.Message.chat.id || variant
  text = 'Hello, bro'
  await bot.send_message(chat_id, text)

executor.start_polling(dp)