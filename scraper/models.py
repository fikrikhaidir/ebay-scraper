from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=120)
    cart = models.ForeignKey('ShoppingCart',null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.user.username
