import requests

def search_youtube_songs(query):
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