from django.contrib import admin
from .models import Category,SubCategory,  Brend, Products
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brend)
admin.site.register(Products)