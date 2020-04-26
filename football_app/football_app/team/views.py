from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets
from rest_framework import mixins
from football_app.team.models import Team
from football_app.team.serializers import TeamShortSerializer, TeamFullSerializer
from django.db.models import Count


class TeamListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.action == 'retrieve':
            queryset = Team.objects.annotate(players_count=Count('players'))
        else:
            queryset = Team.objects.all()
        return queryset

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeamFullSerializer
        else:
            return TeamShortSerializer

    @action(methods=['GET'], detail=False)
    def top(self, request):
        self.queryset = Team.objects.top_three()
        return self.list(request)

    @action(methods=['GET'], detail=False)
    def top_wins(self, request):
        self.queryset = Team.manager2.top_wins()
        return self.list(request)

    @action(methods=['GET'], detail=False)
    def top_losts(self, request):
        self.queryset = Team.manager3.top_losts()
        return self.list(request)
