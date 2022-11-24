from rest_framework import viewsets
from levels.models import Level
from levels.serializers import LevelSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer




