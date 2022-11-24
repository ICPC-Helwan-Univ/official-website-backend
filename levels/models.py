from django.db import models
from model_utils.models import TimeStampedModel


class Level(TimeStampedModel):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    order = models.IntegerField()
