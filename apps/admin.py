from django.contrib import admin
from utils.admin import BaseAdmin
from .models.currency import Currency
from .models.address import Address

# Register your models here.
admin.site.register(Currency, BaseAdmin)
admin.site.register(Address, BaseAdmin)