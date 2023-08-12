import asyncio
import requests
from django.core.exceptions import ObjectDoesNotExist
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from bs4 import BeautifulSoup

from product.models import Shoes

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.reply_to(message, 'Минуточку...')
    loop = asyncio.get_event_loop()
    inn, not_inn = await loop.run_in_executor(None, scrape_and_save)
    await bot.reply_to(message, f'Добавлено товаров {inn}, не добавлено {not_inn} дорогих товаров')


def scrape_and_save():
    for i in range(1, 6):
        url = f'https://superstep.ru/catalog/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&how=r&PAGEN_2={i}'
        req = requests.get(url)
        src = req.text

        soup = BeautifulSoup(src, features="html.parser")
        all_products = soup.find_all(class_='product-item-wrapper js-product-wrapper')
        inn = 0  # счетчик показывает сколько товаров добавилось
        not_inn = 0  # счетчик показывает количество дорогих

        for product in all_products:
            img = 'https://superstep.ru' + product.find('img', class_='product-item-image product-item-image_first')['src']
            url = 'https://superstep.ru' + product.find('a', class_='cur_p js-catalog-card-click')['href']
            price = product.find('span', class_='product-sale-price').text[:-4].replace(' ', '')
            if int(price) <= 16000:
                try:
                    Shoes.objects.get(url=url)  # знаю что лучше в модели добавить unique

                except ObjectDoesNotExist:
                    Shoes.objects.create(
                        img=img,
                        url=url,
                        price=price,
                    )
                    inn += 1
            else:
                not_inn += 1
    return inn, not_inn

