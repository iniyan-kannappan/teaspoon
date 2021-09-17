from django.shortcuts import render, redirect
from teaspoon_app.models import base_drink, topping, line_item, order
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html",{})

@login_required
def menu(request):
    all_drinks=base_drink.objects.all()
    cart = line_item.objects.filter(manage=request.user, order__isnull=True)
    return render(request, 'menu.html', {'all_drinks':all_drinks,'cart':cart})

@login_required
def show_cart(request):
    if request.method == 'POST':
        # When user hits checkout button, control comes here
        cart=line_item.objects.filter(manage=request.user,order__isnull=True)
        order_item = order(manage=request.user)
        order_item.save()
        for item in cart:
            item.order=order_item
            item.save()
        return redirect('menu')
    else:
        cart=line_item.objects.filter(manage=request.user, order__isnull=True)
        return render(request, 'show_cart.html', {"cart":cart})

@login_required
def drink_prep(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        drink=base_drink.objects.get(pk=id)
        price=float(drink.price)*quantity
        print(request.POST.get('honey'))
        if request.POST.get('honey')=='on':
            topping_id=2
        elif request.POST.get('no')=='on':
            topping_id=1
        elif request.POST.get('double')=='on':
            topping_id=3
        elif request.POST.get('triple')=='on':
            topping_id=4
        else:
            topping_id=2
        topping_model=topping.objects.get(pk=topping_id)
        line_item_model=line_item(drink_id=drink,manage=request.user,toppings=topping_model,name=drink.name,quantity=quantity,price=price)
        line_item_model.save()
        return redirect('menu')
    else:
        drink=base_drink.objects.get(pk=id)
        return render(request, "drink_prep.html", {'drink':drink})

@login_required
def orders(request):
    orders=order.objects.all()
    return render(request, 'orders.html', {'orders':orders})

@login_required
def staff_cart(request, order_id):
    order_obj=order.objects.get(pk=order_id)
    drinks_in_order=line_item.objects.filter(order=order_obj)
    return render(request, "staff_cart.html", {'drinks_in_order':drinks_in_order})

@login_required
def done(request, id):
    drink=line_item.objects.get(pk=id)
    drink.done=True
    drink.save()
    return redirect('menu')