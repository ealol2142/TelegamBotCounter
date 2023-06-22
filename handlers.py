import keyboards
from loader import dp, types, bot
import text
import config

import time
import requests
from PIL import Image, ImageFilter
import secrets
import io
import os

# Main menu handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("...", reply_markup=keyboards.removeKey)
    time.sleep(1)
    await message.answer(text.welcome_text1)
    time.sleep(1)
    await message.answer(text.welcome_text2)
    time.sleep(1)
    await message.answer(text.welcome_text3)
    time.sleep(1)
    await message.answer(text.welcome_text4, reply_markup=keyboards.mainKey)

# WebApp response handler
a = []

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    a.clear()
    a.append(message.web_app_data.data)
    await message.answer(text.web_app_data)

# Image response handler
@dp.message_handler(content_types=['photo'])
async def process_photo(message: types.Message) -> None:
    if a:
        print(a)
        file_id = message.photo[2].file_id
        resp = requests.get(config.URI_INFO + file_id)
        img_path = resp.json()['result']['file_path']
        img = requests.get(config.URI+img_path)
        img = Image.open(io.BytesIO(img.content))
        img = img.filter(ImageFilter.GaussianBlur(radius=20))
        if not os.path.exists('static'):
            os.mkdir('static')
        img_name = secrets.token_hex(8)
        img.save(f'static/{img_name}.png', format='PNG')
        a.clear()
        await message.answer_photo(photo=open(f'static/{img_name}.png', 'rb'))
        await message.answer('Оцените', reply_markup=keyboards.surveyKey)
    else:
        await message.answer(text.error_message, reply_markup=keyboards.choiceKeys)


# Inline back button handler
@dp.callback_query_handler(text='back')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text.welcome_text4, reply_markup=keyboards.mainKey)

# Back button reply handler
@dp.message_handler(text='Отмена')
async def some_func(message: types.Message):
    await message.answer("...", reply_markup=keyboards.removeKey)
    time.sleep(1)
    await message.answer(text.welcome_text4, reply_markup=keyboards.mainKey)

# Help menu handler
@dp.callback_query_handler(text='help')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text.help_text, reply_markup=keyboards.backKey)

# WebApp response menu handler
@dp.callback_query_handler(text='choiser')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text.response_menu, reply_markup=keyboards.choiceKeys)

# Like handler
@dp.callback_query_handler(text='like')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    print('like')
    await bot.send_message(callback_query.from_user.id, 'Спасибо!', reply_markup=keyboards.choiceKeys)

# Dislike handler
@dp.callback_query_handler(text='dislike')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    print('dislike')
    await bot.send_message(callback_query.from_user.id, "Спасибо!", reply_markup=keyboards.choiceKeys)


