from aiogram.dispatcher.filters.state import StatesGroup, State

class currency_tenge(StatesGroup):
  currency_korona = State()
  currency_cash = State()