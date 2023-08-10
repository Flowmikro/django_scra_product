from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup

from product.models import Shoes


class Command(BaseCommand):
    # логика команд
    def handle(self, *args, **options):

        # собираем html
        html = urlopen('#')