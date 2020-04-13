from rest_framework import viewsets, mixins
from football_app.player.models import Player
from football_app.player.serializers import PlayerSerializer


class PlayerListViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerStatisticsViewSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin):
    queryset = Player
