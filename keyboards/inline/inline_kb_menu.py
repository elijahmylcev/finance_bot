from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(
  row_width=2,
  inline_keyboard=[
    [
      InlineKeyboardButton(text='Конвертер валюты', callback_data='converter'),
      InlineKeyboardButton(text='Ссылка на дашборд', url='https://google.com')
    ],
    [
      InlineKeyboardButton(text='Записать расходы', callback_data='-')
    ],
    [
      InlineKeyboardButton(text='Записать доходы', callback_data='+')
    ]
  ])
