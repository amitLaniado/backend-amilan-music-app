# import yt_dlp

# async def get_search_results(song_name):
#     with yt_dlp.YoutubeDL() as ydl:
#         search_results = ydl.extract_info(f"ytsearch1:{song_name}", download=False)
#         return search_results

import requests

def search_youtube_songs(query, youtube_api_key):
    print("In search_youtube_songs")
    youtube_search_url = "https://www.googleapis.com/youtube/v3/search"
    
    youtube_params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 10,
        "key": "AIzaSyAGSeY-PSmVhutAdGMb9tKOWN6-HR-OTUU"
    }
    
    response = requests.get(youtube_search_url, params=youtube_params)
    data = response.json()

    print(f"data: {data}")
    
    return data

# Example usage
# youtube_api_key = "YOUR_YOUTUBE_API_KEY"
# query = "Shape of You"
# songs = search_youtube_songs(query, youtube_api_key)
# for song in songs:
#     print(song)
