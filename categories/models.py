from django.db import models

from djangoProject.helpers import get_image_upload_to_path


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=5000)
    color = models.CharField(max_length=7, default='#000000')
    image = models.ImageField(upload_to=get_image_upload_to_path('categories'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
