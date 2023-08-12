from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handlers(commands=['start'])
async def start(message):
    await bot.reply_to(message, 'hello')
