from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = config('API_TOKEN')

bot = Bot(token=TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

admins = [6896900558, ]