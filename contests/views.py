from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contests.models import Contest
from contests.serializers import ContestSerializer


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
