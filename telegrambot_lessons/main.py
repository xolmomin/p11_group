import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import settings
import csv

logging.basicConfig(level=logging.INFO)

bot = Bot(settings.BOT_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


def get_regions():
    with open('regions.csv', encoding='utf-8-sig') as f:
        f.readline()
        data = {k: v for k, v in csv.reader(f)}
        return data


def get_districts():
    with open('districts.csv', encoding='utf-8-sig') as f:
        f.readline()
        return list(csv.reader(f))


regions = get_regions()
districts = get_districts()


class Form(StatesGroup):
    name = State()
    age = State()
    region = State()
    district = State()


@dp.message_handler(commands=['start'])
async def start_menu(message: Message):
    await Form.name.set()
    await message.answer('Xush kelibsiz\nRuyhatdan otish uchun ismingizni kiriting!')


@dp.message_handler(state=Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.next()
    await message.answer('Yoshingizni kiriting')


@dp.message_handler(lambda msg: not msg.text.isdigit(), state=Form.age)
async def get_username(message: Message):
    await message.answer('Yoshni togri kiriting (son bilan)')


async def region_buttons():
    ikm = InlineKeyboardMarkup(row_width=1)
    ikm.add(*[InlineKeyboardButton(name, callback_data=_id) for _id, name in regions.items()])
    return ikm


async def district_buttons(region_id: None):
    ikm = InlineKeyboardMarkup(row_width=1)
    ikm.add(*[InlineKeyboardButton(district[1], callback_data=district[0]) for district in districts if
              district[2] == region_id])
    return ikm


@dp.message_handler(lambda msg: msg.text.isdigit(), state=Form.age)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()
    ikm = await region_buttons()
    await message.answer('Viloyatlarni kiriting', reply_markup=ikm)


@dp.callback_query_handler(state=Form.region)
async def get_region(callback: CallbackQuery, state: FSMContext):
    region = regions.get(callback.data)
    await state.update_data(region=region)
    await Form.next()
    ikm = await district_buttons(callback.data)
    await bot.edit_message_text('Tumanni tanlang', callback.from_user.id, callback.message.message_id, reply_markup=ikm)


@dp.callback_query_handler(state=Form.district)
async def get_username(callback: CallbackQuery, state: FSMContext):
    district_id = callback.data
    district = None
    for district in districts:
        if district[0] == district_id:
            district = district[1]
            break
    await callback.message.delete()
    async with state.proxy() as data:
        data['district'] = district
        text = md.text(
            md.text(md.code('Sizning malumotlaringiz')),
            md.text(md.bold('Ism:'), data['name']),
            md.text(md.bold('Yoshi:'), data['age']),
            md.text(md.bold('Viloyati:'), data['region']),
            md.text(md.bold('Tumani'), data['district']),
            sep='\n'
        )
        await callback.message.answer(text, parse_mode=ParseMode.MARKDOWN)

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# itertools, collections, httpx, asyncpg, aiopg, psycopg2
# pyrogram
