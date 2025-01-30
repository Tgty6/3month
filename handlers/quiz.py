from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import os



async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='button1')
    keyboard.add(button)

    question = 'RM or Barcelona'
    answer = ['RM', 'Barcelona', 'Оба']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )



async def quiz_2(call: types.CallbackQuery):
    question = 'Dota2 or CS.GO'
    answer = ['Dota2', 'CS.GO']

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='button2')
    keyboard.add(button)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Эх ты...',
        open_period=60,
        reply_markup=keyboard)


async def quiz_3(call: types.CallbackQuery):

    photo_path = os.path.join('media','img.png')
    photo = open(photo_path, 'rb')
    await bot.send_photo(chat_id=call.from_user.id,
                             photo=photo)

    question = 'War Thunder or World of Tanks'
    answer = ['War Thunder', 'World of Tanks']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Эх ты...',
        open_period=60)



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button1')
    dp.register_callback_query_handler(quiz_3, text='button2')
