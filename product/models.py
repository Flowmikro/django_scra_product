from django.db import models


class Shoes(models.Model):
    img = models.ImageField(blank=True)
    url = models.CharField(max_length=350)
    price = models.CharField(max_length=150)

    def __str__(self):
        return str(self.url)


