from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('teaspoon_app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
