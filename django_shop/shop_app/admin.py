from django.contrib import admin

# Register your models here.
from shop_app.models import Client, Goods, Order

admin.site.register(Client)
admin.site.register(Goods)
admin.site.register(Order)