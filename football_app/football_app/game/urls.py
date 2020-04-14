from django.urls import path
from football_app.game import views
urlpatterns = [
    path('', views.game_list),
    path('<int:num>/', views.game_detail),
    path('<int:num>/goals/', views.game_goals)
]
