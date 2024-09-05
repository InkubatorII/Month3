from decouple import config
import logging
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os


TOKEN = config('API_TOKEN1')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [6896900558, ]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот включен!',
                               reply_markup=start_test)

# Запуск бота
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello',
                           reply_markup=start)
    # await message.answer(text='Привет')


# Обработчик картинок- Отправляет только определенную картинку
@dp.message_handler(commands=['img'])
async def mem_handler(message: types.Message):
    folder = 'pictures'

    photo_path = os.path.join(folder, 'asd.jpeg')

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo)

# Обработчик картинок - отправляет все картинки
@dp.message_handler(commands=['img_all'])
async def mem_all_handler(message: types.Message):
    folder = 'pictures'
    photos = os.listdir(folder)

    for photo_name in photos:
        photo_path = os.path.join(folder, photo_name)

        if photo_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            with open(photo_path, 'rb') as photo:
                await bot.send_photo(message.from_user.id, photo)

# Обработчик медиа
@dp.message_handler(commands=['music'])
async def music_handler(message: types.Message):
    folder = 'music'
    music_name = 'mihail.mp3'

    music_path = os.path.join(folder, music_name)

    with open(music_path, 'rb') as music:
        await message.answer_audio(music)


# Обработчик для команды отправки файла
@dp.message_handler(commands=['send'])
async def sendfile_handler(message: types.Message):
    # Укажите путь к файлу, который нужно отправить
    file_path = os.path.join(os.getcwd(), 'docs', 'dz.docx')

    if os.path.exists(file_path):
        file_to_send = InputFile(file_path)
        await bot.send_document(message.chat.id, file_to_send)
    else:
        await message.reply("Файл не найден.")

@dp.message_handler()
async def handle_message(message: types.Message):
    user_message = message.text
    if user_message.isdigit():  # Если это число
        number = int(user_message)
        squared_number = number ** 2
        await message.reply(f"Квадрат числа: {squared_number}")
    else:  # Если это не число, просто отправляем эхо
        await message.reply(user_message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)