from django.shortcuts import render, redirect
from teaspoon_app.models import base_drink, topping, line_item
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html",{})

@login_required
def menu(request):
    all_drinks=base_drink.objects.all()
    cart_len=len(line_item.objects.all())
    return render(request, 'menu.html', {'all_drinks':all_drinks,'c_len':cart_len})

@login_required
def show_cart(request):
    if request.method == 'POST':
        cart=line_item.objects.filter(manage=request.user)
        for item in cart:
            item.order_status=True
            item.save()
        return redirect('menu')
    else:
        cart=line_item.objects.filter(manage=request.user)
        cart_len=len(cart)
        return render(request, 'show_cart.html', {"cart":cart})

@login_required
def drink_prep(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        drink=base_drink.objects.get(pk=id)
        price=float(drink.price)*quantity
        line_item_model=line_item(order_status=False,drink_id=drink,manage=request.user,name=drink.name,quantity=quantity,price=price)
        line_item_model.save()
        return redirect('menu')
    else:
        drink=base_drink.objects.get(pk=id)
        return render(request, "drink_prep.html", {'drink':drink})