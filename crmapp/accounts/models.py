from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone =models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(default="profile.png",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORYS = (
        ('Indoor','Indoor'),
        ('Out of door','Out of door')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORYS)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name + "-" + str(self.price)

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name + "-" + str(self.product.price)

