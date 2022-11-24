from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from training_level.models import TrainingLevel
from training_level.serializers import TrainingLevelSerializer


# Create your views here.

class TrainingLevelViewSet(viewsets.ModelViewSet):
    queryset = TrainingLevel.objects.all()
    serializer_class = TrainingLevelSerializer




