import requests
import time as get_time
import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect

song_language="Telugu"


def get_data(theme):
    # Now using youtube v3 apis
    url = "https://www.googleapis.com/youtube/v3/search?maxResults=30&q={}&type=video&key=AIzaSyD8OlFQvf8f6dXuYRSCekWHy9x9gTJjDyU".format(theme+" songs in "+song_language)
    response = requests.get(url)
    data=json.loads(response.text).get("items")
    video_ids=["https://www.youtube.com/embed/"+video_data.get("id").get("videoId") for video_data in data]
    return video_ids


def index(request):
    return render(request,'homepage.html')


def time(request):
    theme=""
    t = get_time.localtime()
    current_time =int(get_time.strftime("%H", t))
    if current_time>=0 and current_time<6:
        theme="Devotional"
    elif current_time>=6 and current_time<12:
        theme="Love"
    elif current_time>=12 and current_time<18:
        theme="Sad"
    else:
        theme="Item"
    links=get_data(theme)
    return render(request,'index.html',{'theme':theme,'page_obj':links,'language':song_language})


def weather(request,weather_type):
    links=get_data(weather_type)
    return render(request,'index.html',{'theme':weather_type,'page_obj':links,'language':song_language})


def happy(request):
    theme="Happyness"
    links=get_data(theme)
    return render(request,'index.html',{'theme':theme,'page_obj':links,'language':song_language})


def sad(request):
    theme="Sad"
    links=get_data(theme)
    return render(request,'index.html',{'theme':theme,'page_obj':links,'language':song_language})


def angry(request):
    theme="Comedy"
    links=get_data(theme)
    return render(request,'index.html',{'theme':theme,'page_obj':links,'language':song_language})


def change_launguage(request,lan):
    global song_language
    song_language=lan
    if(request.META.get('HTTP_REFERER')):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect("/")


def song_search(request):
    theme=""
    if request.method=="POST":
        theme=request.POST.get("theme")
    links=get_data(theme)
    return render(request,'index.html',{'theme':theme,'page_obj':links,'language':song_language})
