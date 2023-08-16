from django.db import models


class Shoes(models.Model):
    """Модель для добавления товаров"""
    img = models.ImageField(upload_to='products/', blank=True)
    url = models.CharField(max_length=350, unique=True)
    price = models.CharField(max_length=150)

    def __str__(self):
        return str(self.url)


