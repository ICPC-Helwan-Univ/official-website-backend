from rest_framework.viewsets import ModelViewSet

from votes.models import Vote
from votes.serializers import VoteSerializer


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
