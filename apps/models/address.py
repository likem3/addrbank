from django.db import models
from utils.models import BaseModel
from .currency import Currency

class Address(BaseModel):
    address = models.CharField(max_length=255, unique=True, help_text="unique currency address")
    phrase = models.TextField(null=True, blank=True, help_text="wallet pharse")
    resource = models.TextField(null=True, blank=True, help_text="resource app of the wallet or url")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="address", help_text="cryptocurrency of the address")
    is_used = models.BooleanField(default=False, help_text="address in use or not")
    merchant_code = models.PositiveIntegerField(null=True, blank=True, help_text="merchant code use the address")
    user_id = models.PositiveIntegerField(null=True, blank=True, help_text="user id use the address")
    label = models.CharField(max_length=255, null=True, blank=True, help_text="remark for the address")

    def __str__(self):
        return f"{self.address} - {self.currency.symbol} - {self.currency.std}"

    class Meta:
        db_table = "apps_addresses"