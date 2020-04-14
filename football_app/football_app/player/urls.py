from django.urls import path
from rest_framework.routers import DefaultRouter
from football_app.player.views import PlayerListViewSet

router = DefaultRouter()
router.register(r'', PlayerListViewSet)
urlpatterns = router.urls
