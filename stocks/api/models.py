from django.db import models

# Create your models here.

class Stocks(models.Model):
    date = models.DateField()
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    close = models.BooleanField()
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol