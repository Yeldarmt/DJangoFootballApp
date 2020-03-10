from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from football_app.country.views import CountryListView

router = DefaultRouter()
router.register(r'', CountryListView,)

urlpatterns = [

]

urlpatterns =urlpatterns + router.urls