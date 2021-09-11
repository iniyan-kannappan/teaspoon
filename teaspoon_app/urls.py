from teaspoon_app import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('menu', views.menu, name="menu"),
    path('drink/<id>', views.drink_prep, name="drink_prep"),
    path('show_cart', views.show_cart, name='show_cart'),
]
