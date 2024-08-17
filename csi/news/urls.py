from django.urls import path
from. import views

urlpatterns=[
    path('', views.news, name="home-news"),
    path('newsview/<str:year>/<int:myid>/<str:slug>', views.newsview, name="home-newsview"),
]