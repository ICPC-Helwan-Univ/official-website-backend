from rest_framework import serializers

from contests.models import Contest


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ['name', 'level', 'start_time', 'end_time', 'is_active', 'prizes', 'password']
