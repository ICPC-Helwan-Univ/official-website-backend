from django.db import models
from model_utils.models import TimeStampedModel

from blog.models import Post


class Vote(TimeStampedModel):
    class VoteType(models.TextChoices):
        UP = 'U', 'up'
        DOWN = 'D', 'down'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=VoteType.choices)

    def __str__(self):
        return f'voted for {self.post}'