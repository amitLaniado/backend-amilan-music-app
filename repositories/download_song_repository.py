import yt_dlp
import tempfile
from data import ydl_opts
import os

def get_mp3_content():
    cwd = os.getcwd()
    songs_directory = f"{cwd}\\songs_downloaded"
    files = os.listdir(songs_directory)

    if len(files) > 0:
        filename = files[0]
        song_path = os.path.join(songs_directory, filename)
        with open(song_path, 'rb') as mp3_file:
            mp3_content = mp3_file.read()
        os.remove(song_path)
        return mp3_content
    else:
        print("No files found in the directory.")
        return None

async def download_song(song_url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
    except Exception as e: 
        print(f"Error downloading song: {e}")
        return None

async def handle_download_song(song_url):
    # with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
    await download_song(song_url)
    song_data = get_mp3_content()
    return song_data