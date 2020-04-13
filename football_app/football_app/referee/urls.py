from django.urls import path
from football_app.referee.views import RefereesListView, RefereeDetailView

urlpatterns = [
    path('', RefereesListView.as_view()),
    path('<int:pk>/', RefereeDetailView.as_view())
]