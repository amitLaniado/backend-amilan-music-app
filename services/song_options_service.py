from repositories.song_options_repository import search_youtube_songs

def arrange_songs_data(songs_data):
    songs = []
    for item in songs_data.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        video_url = f"http://www.youtube.com/watch?v={video_id}"
        
        song_info = {
            "title": title,
            "channel": channel,
            "url": video_url
        }
        songs.append(song_info)
    
    return songs


async def fetch_song_options(song_name):
    print("fetch_song_options")
    search_results = search_youtube_songs(song_name)
    return arrange_songs_data(search_results)