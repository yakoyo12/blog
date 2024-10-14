from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from datetime import datetime


#match_live=1&


def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    #url = "https://apiv3.apifootball.com/?action=get_events&match_live=1&league_id=153&from=2024-09-21&to=2024-09-21&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42"
    #2 url = "England https://apiv3.apifootball.com/?action=get_events&league_id=153&from=2024-10-05&to=2024-10-07&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42"
    url = "https://apiv3.apifootball.com/?action=get_events&match_live=1&league_id=152&from=2024-10-10&to=2024-10-10&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42"
    #url = "https://apiv3.apifootball.com/?action=get_events&match_live=1&league_id=153&from="+today+"&to="+today+"&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request, "index.html", {'jsonResponse':jsonResponse})

def specific(request):
    return HttpResponse("list")

def article(request,article_id):
    return render(request, "index.html",{'article_id':article_id})

def contact(request):
    return render(request, 'contact.html')


#m=2024-09-20&to=2024-09-20&APIkey=94da2ded09https://apiv3.apifootball.com/?action=get_events&league_id=153&fro9e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42

# Create your views here.
