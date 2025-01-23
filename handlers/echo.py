from aiogram import Dispatcher, types
from config import bot


# @dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)



def register_handler(dp: Dispatcher):
    dp.register_message_handler(echo_handler)


