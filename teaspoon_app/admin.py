from django.contrib import admin
from teaspoon_app.models import topping,base_drink,line_item, order, line_item_topping

admin.site.register(topping)
admin.site.register(base_drink)
admin.site.register(line_item)
admin.site.register(order)
admin.site.register(line_item_topping)