from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')

start.add(start_buttons, mem_buttons, mem_all_buttons, music_buttons)

#2 способ добавления кнопок

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
KeyboardButton('/start')

)
#
# #3 способ
# start_test_1 = ReplyKeyboardMarkup(
#     resize_keyboard=True,
#     row_width=2
#     )
#
# start_test_1.add(
#     KeyboardButton('/start'),
#     KeyboardButton('/mem'),
#     KeyboardButton('/mem_all'),
#     KeyboardButton('/music')
# )