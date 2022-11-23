from rest_framework import serializers

from votes.models import Vote


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'