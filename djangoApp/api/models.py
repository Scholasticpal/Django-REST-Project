from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=122)
    price = models.DecimalField(max_digits=10, decimal_places=2)