from django.contrib import admin

from comments.models import Comment
from .models import Post

# Register your models here.
admin.site.register([Post, Comment])