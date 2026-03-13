from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('research/', views.research, name='research'),
    path('teaching/', views.teaching, name='teaching'),
    path('awards/', views.awards, name='awards'),
    path('contact/', views.contact, name='contact'),
]
