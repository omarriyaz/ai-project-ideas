# Fetching video IDs from YouTube Data API based on the search queries.

import requests

API_KEY = ''
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

def fetch_videos(field):
    # Define multiple search queries
    search_query = f"{field} project ideas"
    video_ids = []

    params = {
        'part': 'snippet', # 'snippet' includes basic information like title, description, and thumbnails
        'q': search_query,
        'type': 'video',
        'maxResults': 3,  # Number of videos to fetch per search query
        'key': API_KEY
    }
    # Make a GET request to the YouTube Data API
    response = requests.get(BASE_URL, params=params)

    # Processing the API response
    videos = response.json().get('items', [])
    
    # Extract video IDs from the response
    video_ids.extend([video['id']['videoId'] for video in videos])

    # Return the list of video IDs
    return video_ids