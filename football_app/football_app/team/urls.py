from rest_framework.routers import DefaultRouter

from football_app.league.views import LeagueListView
from football_app.team.views import TeamListView

router = DefaultRouter()
router.register(r'', TeamListView)

urlpatterns = [

]

urlpatterns =urlpatterns + router.urls