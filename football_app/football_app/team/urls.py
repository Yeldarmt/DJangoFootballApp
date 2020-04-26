from rest_framework.routers import DefaultRouter

from football_app.league.views import LeagueListView
from football_app.team.views import TeamListView
from football_app.team.models import Team

router = DefaultRouter()
router.register(r'', TeamListView, basename=Team)

urlpatterns = [

]

urlpatterns =urlpatterns + router.urls