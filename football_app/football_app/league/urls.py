from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from football_app.league.views import LeagueListView

router = DefaultRouter()
router.register(r'', LeagueListView)

urlpatterns = [

]

urlpatterns =urlpatterns + router.urls