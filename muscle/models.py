from django.db import models
from django.utils import timezone
import datetime

class Part(models.Model):
    name = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=20, unique=True)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Record(models.Model):
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    weight = models.FloatField()
    times = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}kg * {}回".format(self.weight, self.times)

