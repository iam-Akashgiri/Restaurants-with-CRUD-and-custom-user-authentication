from django.contrib import admin
from .models import Categories, Food , Customer, Order, BgImage

# Register your models here.

admin.site.register(Categories)
admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(BgImage)
