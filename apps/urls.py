from django.urls import path
from apps.views import (
    CurrencyListView
)


urlpatterns = [
    path('currencies/', CurrencyListView.as_view()),
]