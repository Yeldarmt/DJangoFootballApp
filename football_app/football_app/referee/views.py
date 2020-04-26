from rest_framework import mixins, generics
from football_app.referee.models import Referee
from football_app.referee.serializers import RefereeFullSerializer


class RefereesListView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin):
    queryset = Referee.objects.all()
    serializer_class = RefereeFullSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RefereeDetailView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Referee.objects.all()
    serializer_class = RefereeFullSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
