import random
from config import bot
from aiogram import types, Dispatcher
import asyncio
games=['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
# Эхо - отвечает тем же текстом
async def echo_handler(message: types.Message):
    await message.answer(message.text)
    text = message.text

    if text.isdigit():
        await message.answer(int(text) ** 2)

    elif text == 'game':
        bot_dice = await bot.send_dice(
            chat_id=message.from_user.id,
            emoji=random.choice(games)
        )
        user_dice = await bot.send_dice(
            chat_id=message.from_user.id,
            emoji=random.choice(games)
        )
        await bot.send_message(chat_id=message.from_user.id, text="Подождите, идет бросок...")
        await asyncio.sleep(4)  # Ждем завершения анимации (примерно 4 секунды)

        if bot_dice.dice.value > user_dice.dice.value:
            await bot.send_message(chat_id=message.from_user.id, text="Бот победил!")
        elif bot_dice.dice.value < user_dice.dice.value:
            await bot.send_message(chat_id=message.from_user.id, text="Вы победили!")
        else:
            await bot.send_message(chat_id=message.from_user.id, text="Ничья!")

    else:
        await message.answer(text)

def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)