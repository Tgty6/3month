# webapp.py
from aiogram import types, Dispatcher


async def reply_webapp(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    geeks_online = types.KeyboardButton('Geeks Online',
                                        web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = types.KeyboardButton('Youtube',
                                   web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    github = types.KeyboardButton('Github', web_app=types.WebAppInfo(url='https://github.com/'))



    keyboard.add(geeks_online, youtube, github)

    await message.answer('Reply Кнопки: ', reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])