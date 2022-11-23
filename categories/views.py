from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer