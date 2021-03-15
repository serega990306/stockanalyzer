from django.db import models
from core.models import UserProfile


class Sector(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Stock(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, blank=True, null=True)
    ticket = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.ticket

    class Meta:
        ordering = ["ticket"]


class Strategy(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    user_profile = models.ManyToManyField(UserProfile)
    stock = models.ManyToManyField(Stock)
    date_created = models.DateField(auto_now_add=True)


class StockGroup(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    user_profile = models.ManyToManyField(UserProfile)
    stock = models.ManyToManyField(Stock)
    date_created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


class StockHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    open_time = models.DateTimeField(auto_now_add=True)
    close_time = models.DateTimeField()
