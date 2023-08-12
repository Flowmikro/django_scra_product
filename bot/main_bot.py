import asyncio
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

from bot.scrape.superstep import scrape_and_save

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Привет!\nБот оп парсингу!\nОтправь команду /начать и парсинг запустится.'
                                            '\nВажно! Парсинг осуществляется с сайта:'
                                            '\nhttps://superstep.ru/')


@bot.message_handler(commands=['начать'])
async def start(message):
    await bot.reply_to(message, 'Минуту...')
    loop = asyncio.get_event_loop()
    count_add_product = await loop.run_in_executor(None, scrape_and_save)
    await bot.reply_to(message, f'Добавлено товаров {count_add_product}')
