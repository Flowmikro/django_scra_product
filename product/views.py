from django.shortcuts import render

from .models import Shoes


def list_shoes(request):
    shoes = Shoes.objects.all()
    return render(request, 'list.html', {'shoes': shoes})
