from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import size_product_keyboard
#FSM - Finite State Machine
class FSMStore(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()

async def start_fsm_reg_store(message: types.Message):
    await message.answer('Введите название товара: ')
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
                                       f'Цена: {data["price"]}\n')
    await state.finish()

def register_fsm_reg_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg_store, commands=['store'])
    dp.register_message_handler(load_name, state=FSMStore.name)
    dp.register_message_handler(load_size, state=FSMStore.size)
    dp.register_message_handler(load_category, state=FSMStore.category)
    dp.register_message_handler(load_price, state=FSMStore.price)
    dp.register_message_handler(load_photo, state=FSMStore.photo, content_types=['photo'])