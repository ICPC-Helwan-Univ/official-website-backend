from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'image', 'color']