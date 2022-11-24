from rest_framework import serializers


from levels.models import Level


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

