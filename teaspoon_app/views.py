from django.shortcuts import render, redirect
from teaspoon_app.models import base_drink, topping, cart_drink
from teaspoon_app.forms import CartDrinkForm


def home(request):
    return render(request, "home.html",{})

def menu(request):
    all_drinks=base_drink.objects.all()
    cart_len=len(cart_drink.objects.all())
    return render(request, 'menu.html', {'all_drinks':all_drinks,'c_len':cart_len})

def show_cart(request):
    cart=cart_drink.objects.all()
    cart_len=len(cart)
    return render(request, 'show_cart.html', {"cart":cart})

def drink_prep(request, id):
    print('Inside drink_prep')
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        drink=base_drink.objects.get(pk=id)
        price=float(drink.price)*quantity
        cart_model=cart_drink(drink_id=drink,quantity=quantity,price=price)
        cart_model.save()
        return redirect('menu')
    else:
        drink=base_drink.objects.get(pk=id)
        return render(request, "drink_prep.html", {'drink':drink})