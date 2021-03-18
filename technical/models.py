from django.db import models
from stock.models import Stock


class Indicator(models.Model):
    name = models.CharField(max_length=30)
    function = models.CharField(max_length=30)


class IndicatorValues(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
