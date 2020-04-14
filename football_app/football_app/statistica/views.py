from django.shortcuts import render
from rest_framework import viewsets, mixins
from football_app.statistica.models import Statistica
from football_app.statistica.serializers import StatisticsSerializer


class StatisticsViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    queryset = Statistica.objects.all()
    serializer_class = StatisticsSerializer
