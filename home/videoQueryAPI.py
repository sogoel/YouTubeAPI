from googleapiclient.discovery import build
from urllib.error import HTTPError
from django.conf import settings
""" YouTube API request query and return result to view home"""
query = build('youtube', 'v3', developerKey=settings.YOUTUBE_DATA_API_KEY)

def getVideosAPI(keyword:str):  
    req = query.search().list(
        part = 'snippet',
        maxResults = '50',
        publishedAfter= '2018-08-08T00:00:00Z',
        q = keyword,
        type = 'video',
        relevanceLanguage = 'en',
        pageToken = ''
    )
        
    try:
       res = req.execute()
    except HTTPError as e:
        print('Error : {0}, reason : {1}'.format(e.status_code, e.error_details))
    return res

  

