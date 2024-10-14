from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
    path('contact', views.contact, name='contact'),
]


#https://apiv3.apifootball.com/?action=get_events&league_id=44&from=2023-04-05&to=2024-09-05&152&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42
#England https://apiv3.apifootball.com/?action=get_events&league_id=153&from=2023-04-05&to=2024-04-05&APIkey=94da2ded099e55d23186caefa71650a59735ab6950fd40295629ef7c3b4b2f42