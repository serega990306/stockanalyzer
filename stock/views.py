from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Sector, Stock, StockHistory
from .serializers import SectorSerializer, StockSerializer, StockHistorySerializer, SectorStockSerializer


class SectorView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class SectorStockView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorStockSerializer


class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockHistoryView(ModelViewSet):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer
