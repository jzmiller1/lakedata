from django.db import models


class DecimalData(models.Model):
    site = models.IntegerField()
    total_p = models.FloatField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    sample_time = models.DateTimeField()
