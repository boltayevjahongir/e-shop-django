from django.shortcuts import render
from .models import Category, Brend, SubCategory, Products
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'index.html')



def shop(request):
    ct = Category.objects.all()
    brend = Brend.objects.all()
    productList = Products.objects.all()


    page = request.GET.get('page', 1)

    paginator = Paginator(productList, 3)
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


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})