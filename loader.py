from aiogram import Bot, Dispatcher, types
import config

bot = Bot(token=config.API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
