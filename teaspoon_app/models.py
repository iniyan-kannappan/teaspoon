from django.db import models
from django.contrib.auth.models import User

class topping(models.Model):
    name=models.CharField(max_length=150)
    price=models.DecimalField(null=True,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name

class base_drink(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(null=True,decimal_places=2,max_digits=10)
    # topping=models.ManyToManyField(topping)

    def __str__(self):
        return self.name

class line_item(models.Model):
    order_status=models.BooleanField(default=False)
    drink_id=models.ForeignKey(base_drink, on_delete=models.CASCADE)
    manage = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True)
    price=models.DecimalField(null=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.id)+" | "+str(self.quantity)+" | "+str(self.price)
