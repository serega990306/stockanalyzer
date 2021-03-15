from rest_framework import mixins, viewsets
from .models import Sector, Stock
from .serializers import SectorSerializer, StockSerializer
from rest_framework.viewsets import ModelViewSet


class SectorListView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

'''
class StockListView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
'''
class StockListView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
