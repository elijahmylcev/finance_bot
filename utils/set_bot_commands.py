from aiogram import types

async def set_default_commands(dp):
  await dp.bot.set_my_commands([
    types.BotCommand('register', 'Регистрация'),
    types.BotCommand('start', 'Запустить бота'),
    types.BotCommand('help', 'Помощь'),
    types.BotCommand('income', 'Записать доходы'),
    types.BotCommand('currency', 'Курс ₸')
  ])
