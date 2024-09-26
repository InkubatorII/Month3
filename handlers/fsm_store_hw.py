from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import db_main
from aiogram.types import ReplyKeyboardRemove


# from db import db_main


class Fsm_Store(StatesGroup):
    name_products = State()
    collection = State()
    size = State()
    category = State()
    price = State()
    product_id = State()
    info_product = State()
    photo_products = State()
    submit = State()


async def start_fsm(message: types.Message):
    await message.answer('Укажите название или бренд товара: ', reply_markup=buttons.cancel_button)
    await Fsm_Store.name_products.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_products'] = message.text

    await message.answer('Какой коллекции?: ')
    await Fsm_Store.next()

async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await message.answer('Введите размер товара: ')
    await Fsm_Store.next()

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Введите категорию товара: ')
    await Fsm_Store.next()


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Введите цену товара: ')
    await Fsm_Store.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Введите артикул (он должен быть уникальным): ')
    await Fsm_Store.next()


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Внесите информацию о продукте: ')
    await Fsm_Store.next()

async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product']=message.text

    await message.answer('Отправьте фото:')
    await Fsm_Store.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer('Верные ли данные ?')
    await message.answer_photo(
        photo=data['photo'],
        caption=f'Название/Бренд товара: {data["name_products"]}\n'
                f'Какой коллекции: {data["collection"]}\n'
                f'Информация о товаре: {data["info_product"]}\n'
                f'Размер товара: {data["size"]}\n'
                f'Категория товара: {data["category"]}\n'
                f'Стоимость: {data["price"]}\n'
                f'Артикул: {data["product_id"]}\n',
        reply_markup=buttons.submit_button)

    await Fsm_Store.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer('Отлично, Данные в базе!', reply_markup=kb)
            await db_main.sql_insert_products(
                name_product=data['name_products'],
                size=data['size'],
                price=data['price'],
                product_id=data['product_id'],
                photo=data['photo']
            )
            await db_main.sql_insert_products_details(
                product_id=data['product_id'],
                category=data['category'],
                info_product=data['info_product']
            )
            await db_main.sql_insert_collection_products(
                product_id=data['product_id'],
                collection=data['collection']
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


def register_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")

    dp.register_message_handler(start_fsm, commands=['store2'])
    dp.register_message_handler(load_name, state=Fsm_Store.name_products)
    dp.register_message_handler(load_collection, state=Fsm_Store.collection)
    dp.register_message_handler(load_size, state=Fsm_Store.size)
    dp.register_message_handler(load_category, state=Fsm_Store.category)
    dp.register_message_handler(load_price, state=Fsm_Store.price)
    dp.register_message_handler(load_product_id, state=Fsm_Store.product_id)
    dp.register_message_handler(load_info_product, state=Fsm_Store.info_product)
    dp.register_message_handler(load_photo, state=Fsm_Store.photo_products, content_types=['photo'])
    dp.register_message_handler(submit, state=Fsm_Store.submit)