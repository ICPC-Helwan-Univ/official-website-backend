from django.db import models

from model_utils.models import TimeStampedModel


# Create your models here.
class Tag(TimeStampedModel):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name