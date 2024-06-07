import yt_dlp
from data import ydl_opts
from repositories.download_song_repository import handle_download_song

async def fetch_download_song(song_url):
    if song_url:
        song_data = await handle_download_song(song_url)
        return song_data
    else:
        return None