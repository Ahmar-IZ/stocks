from django.shortcuts import render
from rest_framework import viewsets
from api.models import Stocks
from api.serializers import StocksSerializer
# Create your views here.

class StocksList(viewsets.ModelViewSet):
    """List of stocks is diplayed"""
    serializer_class = StocksSerializer
    queryset = Stocks.objects.all()


