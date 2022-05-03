import asyncio
from threading import Thread
from django.core import paginator
from django.shortcuts import render
from .videoQueryAPI import *
from .models import Video
from .DBHandler import *
from django.core.paginator import Paginator  
from django.http import JsonResponse
import json
from django.shortcuts import render, HttpResponse

user_search_data=''
def home(request):
    """A basic search API to search the stored videos using their title and description."""
    context = {}
    sortby = '-publishTime'
    if request.method == "POST":
        user_search_data = request.POST['searched']
        paginator_ = Paginator(sort_filter_videos(filter=user_search_data,sort_by=sortby), 12)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        'searched': user_search_data,
        }
        return render(request, 'home/home.html', context)
    else:
        """ At Load , hit Youtube API , add in DB and render the data """
        delete_videos_database()
        data = getVideosAPI('IPL')
        res = data['items']
        add_to_database(res)             
        paginator_ = Paginator(sort_filter_videos(sort_by=sortby), 12)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)        
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        }
        return render(request, 'home/home.html', context)


""" A GET API which returns the stored video data in a  sorted in descending order of published datetime."""
def getAllVideoDataInfo(request): 
    video = list(Video.objects.order_by('-publishTime').values())
    return JsonResponse(video, json_dumps_params={'indent': 2},safe=False)
