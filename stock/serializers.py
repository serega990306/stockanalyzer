from .models import Stock, Sector, StockHistory
from rest_framework import serializers


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class StockMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ['id', 'ticket', 'company']


class SectorStockSerializer(serializers.ModelSerializer):
    stocks = StockMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Sector
        fields = ['id', 'name', 'stocks']


class StockHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = StockHistory
        fields = '__all__'

