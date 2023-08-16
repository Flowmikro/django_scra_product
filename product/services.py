from product.models import Shoes


def _list_shoes_db():
    return Shoes.objects.all()