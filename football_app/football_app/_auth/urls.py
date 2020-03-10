from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from football_app._auth.views import UserCreateView, UserListView

router = DefaultRouter()
router.register(r'users', UserListView,)

urlpatterns = [
    path('register/', UserCreateView.as_view()),

]
urlpatterns=urlpatterns+router.urls
