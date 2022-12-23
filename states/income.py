from aiogram.dispatcher.filters.state import StatesGroup, State

class income(StatesGroup):
  category = State()
  count = State()
  currency = State()