from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


# Create your views here.
def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]

    return render(
        req,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
        },
    )


@login_required
def new(req):
    if req.method == "POST":
        form = NewItemForm(req.POST, req.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = req.user
            item.save()

            return redirect("item:detail", pk=item.pk)
    else:
        form = NewItemForm()

    return render(
        req,
        "item/form.html",
        {
            "form": form,
            "title": "New Item",
        },
    )


@login_required
def delete(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    item.image.delete()  # delete image used by item
    item.delete()

    return redirect("dashboard:index")
