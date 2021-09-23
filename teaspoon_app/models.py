from django.db import models
from django.contrib.auth.models import User

class topping(models.Model):
    name=models.CharField(max_length=150)
    price=models.DecimalField(null=True,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name

class base_drink(models.Model):
    image=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(null=True,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name

class order(models.Model):
    manage=models.ForeignKey(User, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+' | '+str(self.order_date)+' | '+str(self.manage)

class line_item(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,default=None, null=True)
    drink_id=models.ForeignKey(base_drink, on_delete=models.CASCADE)
    manage = models.ForeignKey(User, on_delete=models.CASCADE)
    toppings=models.ManyToManyField(topping)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True)
    price=models.DecimalField(null=True, decimal_places=2, max_digits=10)
    done=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' | '+str(self.order)+" | "+str(self.quantity)+" | "+str(self.price)

# class line_item_topping(models.Model):
#     line_item=models.ForeignKey(line_item, on_delete=models.CASCADE)
#     topping=models.ForeignKey(topping, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.topping.name)