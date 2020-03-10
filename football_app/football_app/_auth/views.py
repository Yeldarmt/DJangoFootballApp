from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser

from football_app._auth.models import MyUser
from football_app._auth.serializer import UserShortSerializer, UserFullSerializer, UserUpdateSerializer


class UserCreateView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer



class UserListView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserFullSerializer
        elif self.action=='update':
            return UserUpdateSerializer
        else:
            return UserShortSerializer