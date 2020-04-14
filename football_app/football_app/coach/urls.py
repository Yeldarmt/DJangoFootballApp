from django.urls import path, include
from football_app.coach import views

urlpatterns = [
    path('', views.Lists.as_view()),
    path('<int:pk>/', views.coach_list_detail),
]
