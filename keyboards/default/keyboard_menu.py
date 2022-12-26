from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='Курс ₮(USDT)'),
      KeyboardButton(text='Курс ₸'),
      KeyboardButton(text='Динамика курса'),
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