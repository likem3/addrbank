from django.urls import path
from apps.views import (
    CurrencyListView,
    CurrencyDetailView,
    AddressRetrieveView
)


urlpatterns = [
    path('currencies/', CurrencyListView.as_view()),
    path('currencies/<int:pk>/', CurrencyDetailView.as_view()),
    path('address/', AddressRetrieveView.as_view()),
]