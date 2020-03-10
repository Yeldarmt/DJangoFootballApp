from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from football_app.coach.models import Coach
from football_app.coach.serializers import ListSerializer

#
# @api_view(['GET','POST'])
# def lists(request):
#     if request.method == 'GET':
#         all_lists = Coach.objects.all()
#         # json_lists=[l.to_json() for l in all_lists]
#         ser=ListSerializer(all_lists,many=True)
#         return Response(ser.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         ser=ListSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         return Response(ser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Lists(mixins.ListModelMixin,
            generics.GenericAPIView,
            mixins.CreateModelMixin):

    queryset = Coach.objects.all()
    serializer_class = ListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if (request.user.is_staff==True):
            return self.create(request, *args, **kwargs)
        else:
            return Response('permission denied!!!',status=status.HTTP_403_FORBIDDEN)



@api_view(['GET','PUT','DELETE'])
def coach_list_detail(request,pk):
    try:
        li = Coach.objects.get(id=pk)
    except Coach.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        ser=ListSerializer(li)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        user=request.user
        if user.is_staff==True:
            ser=ListSerializer(instance=li,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)
        else:
            return Response('Permission denied')
    elif request.method=='DELETE':
        if request.user.is_staff==True:
            li.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('Permission denied')
