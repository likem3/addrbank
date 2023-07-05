from typing import Any
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
    key = fernet_key(app_settings.SAFE_USER_KEY)
    _readonly_fields = ['is_used', 'user_id', 'label', 'status', 'created_by']
    createonly_fields = ['address', 'phrase', 'currency']

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
    createonly_fields = ['status']


class AdminNetwork(BaseAdmin):
    _readonly_fields = ['created_by', 'is_deleted']


admin.site.register(Currency, AdminCurrency)
admin.site.register(Address, AdminAddress)
admin.site.register(Network, AdminNetwork)