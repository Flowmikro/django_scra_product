from django.core.management.base import BaseCommand
import asyncio

from bot.main_bot import bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        asyncio.run(bot.polling())