import requests
from bs4 import BeautifulSoup
import time as get_time
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"
song_language="Telugu"
def get_weather():
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(URL)
    # create a new soup
    soup = BeautifulSoup(html.text, "html.parser")
    return soup.find("span", attrs={"id": "wob_dc"}).text
def get_data(theme):
    url="https://www.youtube.com/results?search_query="+theme+" songs in "+song_language
    response=requests.get(url)
    get_time.sleep(5)
    content=response.text
    total=[]
    soup=BeautifulSoup(content,'html.parser')
    h3_tags=soup.find_all('h3',{"class":"yt-lockup-title"})
    for i in h3_tags:
        if len(i.a["href"])==20:
            total.append("https://www.youtube.com/embed/"+i.a["href"].split("=")[-1])
    #try total[:5] for five songs and return total to return all songs
    return total
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
    # links=[]
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
def weather(request):
    theme=""
    weather_type=get_weather()
    if "cloudy" in weather_type.lower():
        theme="Rain"
    elif "sunny" in weather_type.lower():
        theme="Summer"
    elif "rainy" in weather_type.lower():
        theme="Rain"
    elif "snowy" in weather_type.lower():
        theme="Winter"
    else:
        theme="Weather"
    links=get_data(theme)
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
def happy(request):
    theme="Happyness"
    links=get_data(theme)
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
def sad(request):
    theme="Sad"
    links=get_data(theme)
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
def angry(request):
    theme="Comedy"
    links=get_data(theme)
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
def change_launguage(request,lan):
    global song_language
    song_language=lan
    if(request.META.get('HTTP_REFERER')):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect("/")

def song_search(request):
    theme=""
    if request.method=="GET":
        theme=request.GET.get("theme")
    links=get_data(theme)
    paginator = Paginator(links, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'theme':theme,'page_obj':page_obj,'language':song_language})
