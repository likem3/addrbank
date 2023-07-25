from django.contrib import admin
from utils.admin import BaseAdmin
from .models.currency import Currency
from .models.address import Address
from .models.network import Network
from cryptography.fernet import Fernet
from django.conf import settings as app_settings
from utils.helpers import fernet_key
import base64


class AdminAddress(BaseAdmin):
    list_display = [
        'address',
        'resource',
        'get_currency',
        'get_network',
        'get_std',
        'is_used',
        'merchant_code',
        'user_id',
        'label',
        'created_at',
    ]
    list_per_page = 15
    ordering = ('-created_at',)
    search_fields = ('address','resource', 'merchant_code', 'user_id', 'label')

    key = fernet_key(app_settings.SAFE_USER_KEY)

    _readonly_fields = ['is_used', 'merchant_code', 'user_id', 'label', 'status', 'created_by']
    createonly_fields = ['address', 'phrase', 'currency']

    @admin.display(ordering='currency__blockchain', description='Blockchain')
    def get_currency(self, obj):
        return obj.currency.blockchain

    @admin.display(ordering='currency__network__type', description='Network')
    def get_network(self, obj):
        return obj.currency.network.type

    @admin.display(ordering='currency__std', description='Std')
    def get_std(self, obj):
        return obj.currency.std

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "currency":
            kwargs["queryset"] = Currency.objects.filter(status='active')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            obj.phrase = Address.objects.get(pk=obj.pk).phrase
        else:
            if obj.phrase:
                fernet = Fernet(self.key)
                encrypted_data = fernet.encrypt(obj.phrase.encode('utf-8'))
                obj.phrase = encrypted_data.decode()

            obj.created_by = request.user

        obj.save()


class AdminCurrency(BaseAdmin):
    _readonly_fields = ['created_by', 'is_deleted']


class AdminNetwork(BaseAdmin):
    _readonly_fields = ['created_by', 'is_deleted']


admin.site.register(Currency, AdminCurrency)
admin.site.register(Address, AdminAddress)
admin.site.register(Network, AdminNetwork)