from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('research/', views.research, name='research'),
    path('grants/', views.grants_page, name='grants'),
    path('teaching/', views.teaching, name='teaching'),
    path('supervision/', views.supervision_page, name='supervision'),
    path('service/', views.service, name='service'),
    path('awards/', views.awards, name='awards'),
    path('contact/', views.contact, name='contact'),
]
