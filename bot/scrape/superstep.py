import asyncio
import requests
from django.core.exceptions import ObjectDoesNotExist
from bs4 import BeautifulSoup

from product.models import Shoes


def scrape_and_save():
    for i in range(1, 6):
        url = f'https://superstep.ru/catalog/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&how=r&PAGEN_2={i}'
        req = requests.get(url)
        src = req.text

        soup = BeautifulSoup(src, features="html.parser")
        all_products = soup.find_all(class_='product-item-wrapper js-product-wrapper')
        quantity = 0  # счетчик показывает сколько товаров добавилось

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
                    quantity += 1
    return quantity