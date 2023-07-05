from rest_framework import serializers
from apps.models import Address
from apps.serializers import CurrencySerializer

class AddressSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Address
        fields = (
            'address',
            'user_id',
            'label',
        )