from rest_framework import generics
from apps.models import Currency
from apps.serializers import CurrencySerializer, AddressSerializer


class CurrencyListView(generics.ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.filter(status='active')


class AddressRetrieveView(generics.CreateAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return super().get_queryset()