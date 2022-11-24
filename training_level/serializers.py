from rest_framework import serializers

from training_level.models import TrainingLevel


class TrainingLevelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TrainingLevel
        fields = '__all__'

