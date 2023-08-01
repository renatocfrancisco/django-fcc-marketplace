from django.shortcuts import render, get_object_or_404

from .models import Item

# Create your views here.
def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    
    return render(req, 'item/detail.html', {
        'item': item
    })