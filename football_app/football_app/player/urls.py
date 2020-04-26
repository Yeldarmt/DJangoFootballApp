from django.urls import path
from rest_framework.routers import DefaultRouter
from football_app.player.views import PlayerListViewSet
from football_app.player.models import Player

router = DefaultRouter()
router.register(r'', PlayerListViewSet, basename=Player)
urlpatterns = router.urls
