from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item

# Create your views here.


@login_required
def index(req):
    items = Item.objects.filter(created_by=req.user)
    return render(req, "dashboard/index.html", {"items": items})
