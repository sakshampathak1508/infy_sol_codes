from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('about/',views.about,name="home-about"),
    path('rules/',views.rules,name="rule"),
    path('rules/<int:myid>/<str:slug>',views.rules_view,name="rule_view"),
    path('photographs/',views.photographs,name="home-photographs"),
    path('billiards/',views.billiards,name="home-billiards"),
    path('snooker/',views.snooker,name="home-snooker"),
    path('pool/',views.pool,name="home-pool"),
    path('carrom/',views.carrom,name="home-carrom"),
    path('general-tips/',views.general_tips,name="home-general-tips"),
    path('equipments/',views.equipments,name="home-equipments"),
    path('equipments/<int:myid>/<str:slug>',views.equipments_view,name="home-equipments-view"),
    path('event/',views.events,name="home-event"),
    path('contact/',views.contact,name="home-contact"),
    
    path('titles/<str:category>',views.title,name="home-titles"),
    path('titles/<str:category>/<int:myid>/<str:slug>',views.title_view,name="home-titleview"),
    
    path('csiranking/',views.rankings,name="csirankings"),
    path('csiranking/<int:myid>/<str:slug>',views.rankingview,name="csirankings"),
    # path('csiranking/women/',views.womenrankings,name="home-womenrankings"),
    path('search/',views.search,name="search"),
    path("supportus/", views.supportus, name="supportus"),
    path("books/", views.books, name="books"),
    path("site-terms/", views.site_terms, name="site-terms"),
    path("books/bookview/<int:myid>/<str:slug>", views.bookview, name="books"),
    path("form/coachingprogram", views.coachingprogform, name="coaching-form"),
    path("payment/Alexander-Athletic-Club-All-India-Open-Snooker-Tournament-2021/", views.payment, name="payments"),
    path("handlerequest_tournament/", views.handlerequest_tournament, name="handlerequest_tournament"),
    path("bspai-form/", views.bspai_form, name="bspai_form"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),
    path("payment-events/", views.payment_events, name="payment_events"),
    path("handlerequest_events/<str:slug>", views.handlerequest_events, name="handlerequest_events"),
]