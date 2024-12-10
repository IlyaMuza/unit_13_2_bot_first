import asyncio
import aiogram.types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb_inline = aiogram.types.InlineKeyboardMarkup(row_width = 1)
button_il = aiogram.types.InlineKeyboardButton(text = 'Формулы расчёта', callback_data= 'formulas')
kb_inline.add(button_il)

@dp.message_handler(commands='start')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb_inline)
    print('dzfgdfh')

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    print('call')
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

# @dp.message_handler()
# async def get_start_message(message):
#     await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)