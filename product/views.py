from django.shortcuts import render

from .services import _list_shoes_db


def list_shoes(request):
    """Выводим список товаров"""
    shoes = _list_shoes_db()
    return render(request, 'list.html', {'shoes': shoes})


