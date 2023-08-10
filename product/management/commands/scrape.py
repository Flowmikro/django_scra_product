from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from product.models import Shoes

# сохраняем html на всякий
# url = 'https://superstep.ru/catalog/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8'
#
# req = requests.get(url)
#
# src = req.text
#
# with open('shoes1.html', 'w', encoding="utf-8") as file:
#     file.write(src)

with open('shoes1.html', encoding="utf-8") as file:
    src = file.read()


class Command(BaseCommand):
    # логика команд
    def handle(self, *args, **options):
        # преобразуем в soup-объект
        soup = BeautifulSoup(src, features="html.parser")
        all_products = soup.find_all(class_='product-item-wrapper js-product-wrapper')

        # собираем все данные
        for i in all_products:
            img = 'https://superstep.ru' + i.find('img', class_='product-item-image product-item-image_first')['src']
            url = 'https://superstep.ru' + i.find('a', class_='cur_p js-catalog-card-click')['href']
            price = i.find('span', class_='product-sale-price').text
            Shoes.objects.create(
                img=img,
                url=url,
                price=price,
            )
            print('Все работает')
        self.stdout.write('Работа завершена')