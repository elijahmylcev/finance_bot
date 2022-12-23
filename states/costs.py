from aiogram.dispatcher.filters.state import StatesGroup, State

class costs(StatesGroup):
  category = State()
  count = State()
  currency = State()
  executor = State()
  