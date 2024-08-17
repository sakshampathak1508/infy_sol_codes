from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>', views.profile, name="home-profile"),
    path('referees/', views.allrefs, name="refs-profile"),
    path('coaches/', views.allcoach, name="coach-profile"),
    path('players/<str:gender>/<int:myid>/<str:slug>', views.profileview, name="profileview"),
    path('referees/<int:myid>/<str:slug>', views.refview, name="profile-refview"),
    path('coaches/<int:myid>/<str:slug>', views.coachview, name="profile-coachview"),
    path('form/players/', views.playerFormRequest, name="profile-coachview"),
    path('associations/', views.associations, name="profile-associations"),
    path('associations/<int:myid>/<str:slug>', views.associationsview, name="associations-view"),
    path('clubs/', views.clubs, name="clubs"),
    path('clubs/<int:myid>/<str:slug>', views.clubsview, name="clubs-view"),

]