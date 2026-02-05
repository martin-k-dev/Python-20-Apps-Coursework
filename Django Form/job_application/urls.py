from django.urls import path
from . import views

#4th step (3rd was setting up index.html)
# Didn't work, had to put this into __init__.py

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]
