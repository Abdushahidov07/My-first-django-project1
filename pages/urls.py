from django.urls import path

from .views import *

urlpatterns = [
     path("home/", homePageView, name="home"),
     path("menu/", home2PageView, name="home"),
     path("about/", home3PageView, name="home"),

]

