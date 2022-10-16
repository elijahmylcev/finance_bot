from aiogram import Bot, types, Dispatcher

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Create Dispatcher
dp = Dispatcher(bot)