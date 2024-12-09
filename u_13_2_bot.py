import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''
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
    await message.answer(f'Все говорят "{message.text}"3уч А ты купи слона!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)