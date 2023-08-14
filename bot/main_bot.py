import asyncio
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

from bot.scrape.superstep import scrape_and_save
from bot.keyboards.scrape_kb import scrape_kb

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Привет!\nОтправь команду /начать и парсинг запустится.'
                                            '\nВажно! Парсинг осуществляется с сайта:'
                                            '\nhttps://superstep.ru/',
                                            reply_markup=scrape_kb)


@bot.message_handler(commands=['начать'])
async def start(message):
    await bot.reply_to(message, 'Минуту...')
    loop = asyncio.get_event_loop()
    count_add_product = await loop.run_in_executor(None, scrape_and_save)
    await bot.reply_to(message, f'Добавлено товаров {count_add_product}')


@bot.message_handler()
async def process_other_text_answers(message):
    await bot.send_message(message.chat.id, 'Я довольно ограниченный бот, давайте '
                                            'не отходить от темы?')