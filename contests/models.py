from django.db import models
from model_utils.models import TimeStampedModel

from levels.models import Level


class Contest(TimeStampedModel):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    prizes = models.TextField(blank=True)
    password = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name