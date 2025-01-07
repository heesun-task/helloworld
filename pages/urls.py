from django.urls import path
from .views import homePageView, aboutPageView, heesunPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    # path('heesun/', heesunPageView, name='heesun'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>', results, name='results'),
]