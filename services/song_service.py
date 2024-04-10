import yt_dlp
from data import ydl_opts
from repositories.song_repository import handle_download_song

async def fetch_song(song_name):
    song_url = await song_name_to_url(song_name)

    if song_url:
        song_data = await handle_download_song(song_url)  # Await download_song here
        print(f"fetch_song: song_data = {song_data}")
        return song_data
    else:
        print("fetch_song: return None")
        return None

    # song_url = await song_name_to_url(song_name)
    # song_data = await download_song(song_url)
    # return song_data

async def song_name_to_url(song_name):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch1:{song_name}", download=False)
        if 'entries' in search_results:
            first_result = search_results['entries'][0]
            song_url = first_result['original_url']
            return song_url
        else:
            print("No results found for the given song name.")
            return None
