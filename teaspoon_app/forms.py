from django import forms
from teaspoon_app.models import cart_drink

class CartDrinkForm(forms.ModelForm):
    class Meta:
        model=cart_drink
        fields=['drink_id', 'quantity', 'price']