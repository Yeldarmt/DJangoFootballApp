from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets
from rest_framework import mixins
from football_app.team.models import Team
from football_app.team.serializers import  TeamShortSerializer, TeamFullSerializer


class TeamListView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = Team.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action=='update' or self.action=='destroy':
            permission_classes = [IsAdminUser,]
        else:
            permission_classes = [AllowAny,]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeamFullSerializer
        else:
            return TeamShortSerializer
