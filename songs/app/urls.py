from django.urls import path
from . views import index,time,weather,happy,angry,sad,change_launguage,song_search
app_name="app"
urlpatterns = [
    path('',index,name="index"),
    path('time/',time,name="time"),
    path('weather/<str:weather_type>',weather,name="weather"),
    path('happy/',happy,name="happy"),
    path('sad/',sad,name="sad"),
    path('angry/',angry,name="angry"),
    path('change_launguage/<str:lan>',change_launguage,name="change_launguage"),
    path('song_search/',song_search,name="song_search"),

]
