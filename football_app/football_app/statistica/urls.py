from rest_framework.routers import DefaultRouter
from football_app.statistica.views import StatisticsViewSet

router = DefaultRouter()

router.register(r'', StatisticsViewSet)

urlpatterns = router.urls
