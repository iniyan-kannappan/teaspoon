from teaspoon_app import views
from django.urls import path
from teaspoon_app.views import ShowCart, Menu, Order, DrinkPrep, StaffCart, LineItemDone
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home,name="home"),
    path('menu', Menu.as_view(), name="menu"),
    path('drink/<int:id>', login_required(DrinkPrep.as_view()), name="drink_prep"),
    path('show_cart', login_required(ShowCart.as_view()), name="show_cart"),
    path('orders', login_required(Order.as_view()), name='orders'),
    path('staff_cart/<int:order_id>', login_required(StaffCart.as_view()), name='staff_cart'),
    path('done/<int:id>', login_required(LineItemDone.as_view()), name='done'),
]
