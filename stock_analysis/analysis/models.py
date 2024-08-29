from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    last_quarter_performance = models.FloatField()
    daily_trading_volume = models.BigIntegerField()

    def __str__(self):
        return self.symbol
