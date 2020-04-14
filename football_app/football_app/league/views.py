from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets
from rest_framework import mixins

from football_app.league.models import League
from football_app.league.serializers import LeagueFullSerializer, LeagueShortSerializer


class LeagueListView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = League.objects.all()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LeagueFullSerializer
        else:
            return LeagueShortSerializer
