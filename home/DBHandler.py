from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Video
import asyncio
from .videoQueryAPI import *

def add_to_database(res):
    for result in res:
        snippet = result['snippet']
        formated_date = snippet['publishedAt']
        vid = Video(title= snippet['title'], description= snippet['description'], publishTime= formated_date, thumbnail_url= snippet['thumbnails']['medium']['url'], url= result['id']['videoId'], channelTitle=snippet['channelTitle'])
        print("Added:",vid.title)
        vid.save()
        
def delete_videos_database():
    Video.objects.all().delete()


def sort_filter_videos(filter='',sort_by=''):
    if sort_by == '' and filter == '':
        return Video.objects.all()
    elif sort_by != '' and filter == '':
        return Video.objects.order_by(sort_by)
    elif sort_by == '' and filter != '':
        return Video.objects.filter(Q(title__icontains=filter) | Q(description__icontains=filter))
    else:
        return Video.objects.filter(Q(title__icontains=filter) | Q(description__icontains=filter)).order_by(sort_by)
    
    

