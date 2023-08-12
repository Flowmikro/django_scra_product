import asyncio

import requests
from django.core.exceptions import ObjectDoesNotExist
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from bs4 import BeautifulSoup

from product.models import Shoes

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')

url = 'https://superstep.ru/catalog/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8'

req = requests.get(url)

src = req.text


@bot.message_handler(commands=['start'])
async def start(message):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, scrape_and_save)
    await bot.reply_to(message, 'Готово!')


def scrape_and_save():
    soup = BeautifulSoup(src, features="html.parser")
    all_products = soup.find_all(class_='product-item-wrapper js-product-wrapper')

    for i in all_products:
        img = 'https://superstep.ru' + i.find('img', class_='product-item-image product-item-image_first')['src']
        url = 'https://superstep.ru' + i.find('a', class_='cur_p js-catalog-card-click')['href']
        price = i.find('span', class_='product-sale-price').text[:-4].replace(' ', '')
        if int(price) <= 16000:
            try:
                Shoes.objects.get(url=url)
                print(f"Товар уже есть в базе данных")
            except ObjectDoesNotExist:
                Shoes.objects.create(
                    img=img,
                    url=url,
                    price=price,
                )
                print(f"Товар успешно добавлен в базу данных")
        else:
            print('Товар дорогой')