from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subID = models.ForeignKey(Category, related_name='subcategory',  on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name




class Brend(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    img = models.ImageField(null=True)
    narx = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    chegirma = models.IntegerField(default=0, null=True)
    Condition = models.BooleanField(default=True, null=True)
    Count = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title