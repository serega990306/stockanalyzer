from rest_framework import mixins, viewsets
from .models import Sector, Stock, StockHistory
from .serializers import SectorSerializer, StockSerializer, StockHistorySerializer
from rest_framework.viewsets import ModelViewSet


class SectorListView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class StockListView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockHistoryView(ModelViewSet):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer
