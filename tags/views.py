from rest_framework.viewsets import ModelViewSet


from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = ['name']
    ordering_fields = ['name']