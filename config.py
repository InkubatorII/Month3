from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config('API_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [6896900558, ]