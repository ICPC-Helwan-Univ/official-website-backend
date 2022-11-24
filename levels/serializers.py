from rest_framework import serializers


from levels.models import TrainingLevel


class TrainingLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingLevel
        fields = '__all__'

