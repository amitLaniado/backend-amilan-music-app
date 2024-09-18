import yt_dlp
import tempfile
from data import ydl_opts
import os

def find_first_mp3(strings):
    for string in strings:
        if string.endswith(".mp3"):
            return string
    return None

def get_mp3_content():
    cwd = os.getcwd()
    songs_directory = f"{cwd}/songs_downloaded"
    files = os.listdir(songs_directory)

    # Find the first .mp3 file
    filename = find_first_mp3(files)

    if filename is None:
        print(f"No .mp3 file found in the directory. Files in the directory: {files}")
        return None

    song_path = os.path.join(songs_directory, filename)
    print(f"song_path = {song_path}")

    try:
        with open(song_path, 'rb') as mp3_file:
            mp3_content = mp3_file.read()
        os.remove(song_path)  # Remove the file after reading it
        return mp3_content
    except Exception as e:
        print(f"Error reading or removing the file: {e}")
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