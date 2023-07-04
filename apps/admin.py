from django.contrib import admin
from .models.currency import Currency
from .models.address import Address

# Register your models here.
admin.site.register(Currency)
admin.site.register(Address)