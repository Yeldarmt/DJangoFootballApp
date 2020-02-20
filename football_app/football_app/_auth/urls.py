from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from football_app._auth.views import index

urlpatterns = [
    path('login/', obtain_jwt_token),
]
