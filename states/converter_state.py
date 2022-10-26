from aiogram.dispatcher.filters.state import StatesGroup, State

class converter(StatesGroup):
  currency_current = State()
  price_input = State()