from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers import PostSerializer, PostWithTagsSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('tags').all()
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return PostWithTagsSerializer
        return PostSerializer

    search_fields = ['title', 'content']