from rest_framework import serializers
from apps.models import Currency, Network


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = (
            'name',
            'description',
            'type',
        )


class CurrencySerializer(serializers.ModelSerializer):
    network = NetworkSerializer(read_only=True)
    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
            'symbol',
            'blockchain',
            'std',
            'network'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['std'] = None if not representation['std'] else representation['std'].upper()
        return representation
