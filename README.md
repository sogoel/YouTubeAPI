Youtube Api

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

Project Goals:
● Use YouTube API to fetch list of videos of certain search keyword for fetching the latest videos for a predefined search query and store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database
with proper indexes.
● A GET API which returns the stored video data in a paginated response sorted in
descending order of published datetime.
● A basic search API to search the stored videos using their title and description.
● Project should be scalable and optimized.


The project is based on Django.

Setup Guide

● Clone the project
● Run the server using python mange.py runserver
● To check GET API which returns the stored video data sorted in descending order of published datetime, click on Show all Videos Data Button from header.
● To get result of search API showing stored videos using their title and description,type the query in text form and click on Video Search button.