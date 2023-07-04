from django.db import models
from utils.models import BaseModel

class Currency(BaseModel):
    name = models.CharField(max_length=20, help_text="name of the currency such as bitcoin, ethereum, tron, etc.")
    symbol = models.CharField(max_length=10, help_text="symbol of the currency such as BTC, ETH, TRX, etc.")
    blockchain = models.CharField(max_length=50, help_text="blochain name of the currency such as bitcoin, etherum, tron, etc.")
    std = models.CharField(max_length=20, null=True, blank=True, help_text="standard token of the currency ex ERC20, TRC20, BEP20, etc.")

    def __str__(self):
        return f"{self.name} - {self.symbol} - {self.blockchain} - {(self.std if self.std else '')}"

    class Meta:
        db_table = "apps_currencies"