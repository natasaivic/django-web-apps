from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('experience/', views.experience, name="experience"),
    path('qa/', views.qa, name="questions and answers"),
    path('subscribe_form/', views.subscribe_form, name="subscribe form"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('contact/', views.contact, name="contact"),
]
