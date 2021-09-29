from django.shortcuts import render, redirect
from teaspoon_app.models import base_drink, topping, line_item, order
from django.contrib.auth.decorators import login_required
from django.views import View

@login_required
def home(request):
    return render(request, "home.html",{})

class Menu(View):
    def get(self, request):
        all_drinks=base_drink.objects.all()
        cart = line_item.objects.filter(manage=request.user, order__isnull=True)
        return render(request, 'menu.html', {'all_drinks':all_drinks,'cart':cart})

class ShowCart(View):
    def post(self,request):
        cart=line_item.objects.filter(manage=request.user,order__isnull=True)
        order_item = order(manage=request.user)
        order_item.save()
        for item in cart:
            item.order=order_item
            item.save()
        return redirect('menu')

    def get(self,request):
        cart=line_item.objects.filter(manage=request.user, order__isnull=True)
        for item in cart:
            print(item.id,item.toppings.all())
        return render(request, 'show_cart.html', {"cart":cart})

class DrinkPrep(View):
    def post(self,request,**kwargs):
        quantity = int(request.POST.get('quantity'))
        drink=base_drink.objects.get(pk=kwargs['id'])
        price=float(drink.price)*quantity
        topping_id=[]
        if request.POST.get('honey')=='on':
            topping_id.append(1)
        if request.POST.get('double')=='on':
            topping_id.append(2)
        if request.POST.get('triple')=='on':
            topping_id.append(3)
        print(topping_id)
        line_item_model = line_item(drink_id=drink, manage=request.user, name=drink.name, quantity=quantity, price=price)
        line_item_model.save()
        for id in topping_id:
            _topping=topping.objects.get(pk=id)
            line_item_model.toppings.add(_topping)
        return redirect('menu')

    def get(self,request, **kwargs):
        drink=base_drink.objects.get(pk=kwargs['id'])
        return render(request, "drink_prep.html", {'drink':drink})

class Order(View):
    def get(self,request):
        orders=order.objects.all()
        var=True
        for order_obj in orders:
            drinks=line_item.objects.filter(order=order_obj.id)
            for drink in drinks:
                if not drink.done:
                    var=False
                    break
            if not var:
                break
            if var:
                order_obj.pending_or_dispatched=True
                order_obj.save()
        return render(request, 'orders.html', {'orders':orders})

class StaffCart(View):
    def get(self,request, **kwargs):
        order_obj=order.objects.get(pk=kwargs['order_id'])
        drinks_in_order=line_item.objects.filter(order=order_obj)
        return render(request, "staff_cart.html", {'drinks_in_order':drinks_in_order})

class LineItemDone(View):
    def get(self,request, **kwargs):
        drink=line_item.objects.get(pk=kwargs['id'])
        order_id=drink.order.id
        drink.done=True
        drink.save()
        return redirect('staff_cart',order_id=order_id)