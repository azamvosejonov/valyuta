from aiogram.dispatcher.filters.state import State, StatesGroup

class Valyuta(StatesGroup):
    choice=State()
    amount=State()