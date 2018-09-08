from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('papa/', views.papa, name='papa'),
    path('mama/', views.mama, name='mama')
]
