from aiogram import Dispatcher, types
import os
from config import bot
import random


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')

# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message, photo=None, caption=None):
    photo_path = os.path.join('media', 'img.png')

    photo = open(photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=caption)


async def game(message: types.Message):
    dice_random = random.choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲'])
    await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game, commands=['game'])