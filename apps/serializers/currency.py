from rest_framework import serializers
from apps.models import Currency, Address

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
            'symbol',
            'blockchain',
            'std'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['std'] = None if not representation['std'] else representation['std'].upper()
        return representation
