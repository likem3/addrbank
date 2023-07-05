from django.urls import path
from apps.views import (
    CurrencyListView,
    AddressRetrieveView
)


urlpatterns = [
    path('currencies/', CurrencyListView.as_view()),
    path('address/', AddressRetrieveView.as_view()),
]