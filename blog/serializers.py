from rest_framework import serializers

from blog.models import Post
from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer


class PostSerializerMixin():
    class Meta:
        model = Post
        fields = ['title', 'slug', 'short_description', 'image', 'content', 'category', 'tags']


class PostSerializer(PostSerializerMixin, serializers.ModelSerializer):
    pass


class PostWithTagsSerializer(PostSerializerMixin, serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta(PostSerializerMixin.Meta):
        fields = PostSerializerMixin.Meta.fields + ['url']
