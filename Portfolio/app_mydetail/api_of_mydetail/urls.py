from django.urls import path 
from .import views


urlpatterns = [
    path("", views.home, name="home"),
    path("expertise/", views.Expertise, name="expertise")
]



