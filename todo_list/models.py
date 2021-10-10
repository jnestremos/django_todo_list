from django.db import models
import datetime

class List(models.Model):
    item_name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    event_date = models.DateField()
    event_remarks = models.CharField(max_length=200, null=True)
    pricing = models.DecimalField(max_digits=200, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.event_name
# Create your models here.
