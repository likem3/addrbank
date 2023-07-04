from django.db import models
from utils.models import BaseModel
from .currency import Currency

class Address(BaseModel):
    address = models.CharField(max_length=255, unique=True, help_text="unique currency address")
    phrase = models.TextField(help_text="wallet pharse")
    resource = models.TextField(help_text="resource app of the wallet or url")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="address", help_text="cryptocurrency of the address")

    def __str__(self):
        return f"{self.address} - {self.currency.symbol} - {self.currency.std}"

    class Meta:
        db_table = "apps_addresses"