from django.db import models
from model_utils.models import TimeStampedModel

from categories.models import Category
from djangoProject.helpers import get_image_upload_to_path
from tags.models import Tag


# Create your models here.
class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    short_description = models.CharField(max_length=255)
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to=get_image_upload_to_path('post'))
    tags = models.ManyToManyField(to=Tag, related_name='posts', blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
