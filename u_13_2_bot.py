import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '7704597688:AAEgiaik-tnh3YqW3_8U8qXujRYjKqqOHWY'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    print('Привет! Я бот продающий слона.')
    await message.answer('Привет! Я бот продающий слона.')
    await message.answer('Купи слона!')


@dp.message_handler()
async def start(message):
    print('Пришло:', message.text)
    await message.answer(f'Все говорят "{message.text}" А ты купи слона!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)