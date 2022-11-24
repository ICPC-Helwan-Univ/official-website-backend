from rest_framework import viewsets
from levels.models import TrainingLevel
from levels.serializers import TrainingLevelSerializer


class TrainingLevelViewSet(viewsets.ModelViewSet):
    queryset = TrainingLevel.objects.all()
    serializer_class = TrainingLevelSerializer




