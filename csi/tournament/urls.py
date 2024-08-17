from django.urls import path
from. import views

urlpatterns = [
    path('', views.tournament, name="home-tournament"),
    path('tourview/<str:year>/<int:myid>/<str:slug>', views.tourview, name="tourview"),
    path('event/<str:slug>', views.tour_eve_category, name="toureventview"),
    path('sport/<str:slug>', views.tour_sport_category, name="toursportview"),
    path('event-form', views.tour_form, name="event_form"),
]