from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import size_product_keyboard
from aiogram.types import ReplyKeyboardRemove
from db import db_main
import buttons
#FSM - Finite State Machine
class FSMStore(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()

async def start_fsm_reg_store(message: types.Message):
    await message.answer('Введите название товара: ', reply_markup=buttons.cancel_button)
    await FSMStore.name.set()

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer('Выберите размер товара: ', reply_markup=size_product_keyboard)
    await FSMStore.next()

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Выберите категорию: ')
    await FSMStore.next()

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Установите цену: ')
    await FSMStore.next()

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Установите артикул: ')
    await FSMStore.next()

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Выберите фотографию товара: ')
    await FSMStore.next()

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f'Верные ли данные?\n\n'
                                       f'Название товара: {data["name"]}\n'
                                       f'Размер: {data["size"]}\n'
                                       f'Категория: {data["category"]}\n'
                                       f'Цена: {data["price"]}\n'
                                       f'Артикул: {data["product_id"]}\n',
                                reply_markup = buttons.submit_button
                                )
    await FSMStore.next()
async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
        await message.answer('Отлично, Данные в базе!', reply_markup=kb)
        await db_main.sql_insert_products(
            name_products=data['name_products'],
            size=data['size'],
            category=data['category'],
            price=data['price'],
            product_id=data['product_id'],
            photo=data['photo']
        )
        await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет"')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    kb = ReplyKeyboardRemove()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)


def register_fsm_reg_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_reg_store, commands=['store'])
    dp.register_message_handler(load_name, state=FSMStore.name)
    dp.register_message_handler(load_size, state=FSMStore.size)
    dp.register_message_handler(load_category, state=FSMStore.category)
    dp.register_message_handler(load_price, state=FSMStore.price)
    dp.register_message_handler(load_product_id, state=FSMStore.product_id)
    dp.register_message_handler(load_photo, state=FSMStore.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSMStore.submit)