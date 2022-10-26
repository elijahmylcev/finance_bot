from aiogram.dispatcher.filters.state import StatesGroup, State

class register(StatesGroup):
  write_name = State()
  old = State()