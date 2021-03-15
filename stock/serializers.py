from .models import Stock, Sector
from rest_framework import serializers


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    # sector_name = serializers.CharField(source='sector.name', read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'
