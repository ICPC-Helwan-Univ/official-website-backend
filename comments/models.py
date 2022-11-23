from django.db import models

from blog.models import Post
from model_utils.models import TimeStampedModel


# Create your models here.
class Comment(TimeStampedModel):
    content = models.TextField(max_length=1000)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
