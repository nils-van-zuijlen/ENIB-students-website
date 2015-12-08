from django.db import models


class Note(models.Model):
    foreign_id = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=255)
    mail = models.EmailField()
    note = models.DecimalField(max_digits=10, decimal_places=2)


class HistoryLine(models.Model):
    foreign_id = models.IntegerField()
    date = models.DateTimeField(default=None, null=True, blank=True)
    note = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    price_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    liquid_quantity = models.IntegerField(default=0)
    percentage=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

