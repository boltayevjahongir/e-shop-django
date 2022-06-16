from django.shortcuts import render
from .models import Category, Brend, SubCategory, Products

# Create your views here.
def home(request):
    return render(request, 'index.html')



def shop(request):
    ct = Category.objects.all()
    brend = Brend.objects.all()
    subC = SubCategory.objects.all()
    products = Products.objects.all()
    return render(request, "shop.html", context={
        'ct': ct,
        'brend':brend,
        'subC': subC,
        'products':products
    })




def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})