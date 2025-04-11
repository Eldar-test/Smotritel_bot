
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = "YOUR_BOT_API_TOKEN"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Добро пожаловать в Лабиринт. Я?! Выберите тест из меню ниже.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
