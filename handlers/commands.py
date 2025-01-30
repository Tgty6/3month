# commands.py
from aiogram import Dispatcher, types
import os
from config import bot
import random

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'images.jpeg')

    photo = open(photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это мем')



async def game(message: types.Message):
    dice_random = random.choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲'])
    await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)

    bot_message = await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)
    bot_score = bot_message.dice.value
    print(bot_score)

    user_message = await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)
    user_score = user_message.dice.value
    print(user_score)

    if user_score > bot_score:
        await message.answer('Вы победили')
    elif user_score < bot_score:
        await message.answer('Вы проиграли')
    else:
        await message.answer('Ничья')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game, commands=['game'])