from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard, keyboard1, phone_key, mac_key, cb

from main import bot, dp
from config import chat_id

async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text="Hello")

# @dp.message_handler()
# async def send_answer(message: Message):
#     text = message.text
#     await message.answer(text=text)
#это функ эхо, может вызвать ошибки

#@dp.message_handler(Command('shop'))
@dp.message_handler(commands=['shop'])
async def show_shop(message: Message):
    await message.answer('shop', reply_markup=keyboard)#reply_markup=keyboard

@dp.message_handler(Text(equals=['btn1', 'btn2', 'btn3']))
async def get_goods(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['tshop'])
async def show(message: Message):
    await message.answer(text='Buy or cancel', reply_markup=keyboard1)

@dp.callback_query_handler(text_contains=['phone'])
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Купить', reply_markup=phone_key)

@dp.callback_query_handler(cb.filter(name='macbook'))
async def macbook(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    p = callback_data.get('price')

    await call.message.answer(f'Купить. Цена: {p}', reply_markup=mac_key)

@dp.callback_query_handler(text_contains=['cancel'])
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
