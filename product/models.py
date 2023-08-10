from django.db import models


class Shoes(models.Model):
    img = models.ImageField(upload_to='products/', blank=True)
    url = models.CharField(max_length=350)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)


