from django.shortcuts import redirect, render

from item.models import Category, Item

from .forms import SignupForm

from django.views.decorators.csrf import csrf_protect # because of the post method

# Create your views here.

def index(req):

    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(req, 'core/index.html', {
        'items': items, 
        'categories': categories
    })

def contact(req):
    return render(req, 'core/contact.html')

@csrf_protect # because of the post method
def signup(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(req, 'core/signup.html', {
        'form': form
    })