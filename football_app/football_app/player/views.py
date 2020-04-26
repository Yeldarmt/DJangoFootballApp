from rest_framework import viewsets, mixins
from football_app.player.models import Player
from football_app.player.serializers import PlayerSerializer, PlayerShortSerializer
from football_app.statistica.serializers import StatisticsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PlayerListViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    def get_queryset(self):
        if self.action == 'list':
            queryset = Player.objects.select_related('team')
        else:
            queryset = Player.objects.all()
        return queryset
    permission_classes = ()

    def get_serializer_class(self):
        print('playerSelfAction: ', self.action)
        if self.action == 'list':
            return PlayerShortSerializer
        else:
            return PlayerSerializer

    @action(methods=['GET'], detail=True)
    def get_stata(self, request,  pk):
        try:
            player = Player.objects.get(id=pk)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stata = player.statistica
        serializers = StatisticsSerializer(stata)
        return Response(serializers.data)

    @action(methods=['PUT'], detail=True)
    def update_stata(self, request, pk):
        try:
            player = Player.objects.get(id=pk)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stata = player.statistica
        serializer = StatisticsSerializer(instance=stata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


