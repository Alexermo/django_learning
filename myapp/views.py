from django.shortcuts import render
from .models import Category, Item


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def item_id(request, my_id):
    item = Item.objects.get(id=my_id)
    return render(request, 'item.html', {'item': item})
