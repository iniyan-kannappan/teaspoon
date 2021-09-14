from django.contrib import admin
from teaspoon_app.models import topping,base_drink,line_item

admin.site.register(topping)
admin.site.register(base_drink)
admin.site.register(line_item)

