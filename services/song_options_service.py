from repositories.song_options_repository import search_youtube_songs

# def arrange_entries(entries): 
#     song_options = []

#     for entry in entries: # שים לב: לא יודע למה אבל יש רק entry אחד כל פעם
#         # כלומר לא משנה מה זה מחזיר לי רק אופציה אחת
#         song_option = {
#             'original_url': entry.get('original_url', ''),
#             'title': entry.get('title', ''),
#             'artist': entry.get('artist', '')
#         }
#         song_options.append(song_option)

#     print(f"song_options: {song_options}")
#     return song_options

# async def fetch_song_options(song_name):
#     search_results = await get_search_results(song_name)
#     entries = search_results.get('entries', [])
#     return arrange_entries(entries)

def arrange_songs_data(songs_data):
    songs = []
    for item in songs_data.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        song_info = {
            "title": title,
            "channel": channel,
            "url": video_url
        }
        songs.append(song_info)
    
    return songs


async def fetch_song_options(song_name):
    search_results = await search_youtube_songs(song_name)
    return arrange_songs_data(search_results)