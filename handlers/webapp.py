from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import ChatNotFound

# Reply Keyboard
async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    geeks_online = KeyboardButton('Geeks Online', web_app=types.WebAppInfo(url='https://online.geeks.kg/'))
    youtube = KeyboardButton('YouTube', web_app=types.WebAppInfo(url='https://www.youtube.com/'))
    vk = KeyboardButton('VK', web_app=types.WebAppInfo(url='https://vk.com/'))
    chatgpt = KeyboardButton('ChatGPT', web_app=types.WebAppInfo(url='https://chatgpt.com/'))
    github = KeyboardButton('GitHub', web_app=types.WebAppInfo(url='https://github.com/'))

    keyboard.add(geeks_online, youtube, vk, chatgpt, github)
# Inline Keyboard
async def inline_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    gitignore_io = InlineKeyboardButton('gitignore_io', web_app=types.WebAppInfo(url='https://gitignore.io/'))
    translate = InlineKeyboardButton('translate', web_app=types.WebAppInfo(url='https://translate.google.com/'))
    kaktus_media = InlineKeyboardButton('kaktus.meadia', web_app=types.WebAppInfo(url='https://kaktus.meadia/'))

    keyboard.add(gitignore_io, translate, kaktus_media)

    await message.answer(text='WebApp кнопки:', reply_markup=keyboard)





def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])
    dp.register_message_handler(inline_webapp, commands=['inline_webapp'])
