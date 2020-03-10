
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets, permissions
from rest_framework import mixins

from football_app.country.models import Country
from football_app.country.serializers import CountrySerializer

class CountryListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action=='update' or self.action=='destroy':
            permission_classes = [IsAdminUser,]
        else:
            permission_classes = [AllowAny,]
        return [permission() for permission in permission_classes]

