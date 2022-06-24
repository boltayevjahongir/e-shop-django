import json

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Category, Brend, SubCategory, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import CreateUserForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def shop(request):
    ct = Category.objects.all()
    brend = Brend.objects.all()
    productList = Products.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        catId = json.load(request)['catId']
        productList = Products.objects.filter(category=catId[0])

    page = request.GET.get('page', 1)

    paginator = Paginator(productList, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "shop.html", context={
        'ct': ct,
        'brend': brend,
        'products': products
    })




def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')

            return redirect('home')
        else:
            messages.error(request, 'Errorr')
    return render(request, 'registration/signup.html', context={
        'form': form
    })



def related(request):

    category = Category.objects.all()

    return render(request, 'related.html', context={'categorys':category})

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})
