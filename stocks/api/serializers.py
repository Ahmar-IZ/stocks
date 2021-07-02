from rest_framework import serializers
from api.models import Stocks


class StocksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stocks
        fields = '__all__'