from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class TrainingLevel(TimeStampedModel):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    order = models.IntegerField()
