from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='Инлайн меню'),
      KeyboardButton(text='Курс тенге'),
      KeyboardButton(text='Показать дашборд'),
    ],
    [
      KeyboardButton(text='Записать расходы'),
    ],
    [
      KeyboardButton(text='Записать доходы'),
    ]
  ],
  resize_keyboard=True
)