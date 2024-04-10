import yt_dlp
import tempfile
from data import ydl_opts


async def handle_download_song(song_url):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        await download_song(song_url, tmp_file)
        print(f"tmp_file.name = {tmp_file.name}")

        with open(tmp_file.name, 'rb') as f:
            song_data = f.read()
            print(f"download_song: song_data = {song_data}")
            return song_data



async def download_song(song_url, tmp_file):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ydl.params['out'] = tmp_file.name
            # ydl.download([song_url])

            print(f"ydl.params['outtmpl'] = {ydl.params['outtmpl']}")
            print(f"ydl.title = {ydl.title}")
            print(f"ydl.id = {ydl.id}")
            print(f"ydl.ext = {ydl.ext}")
            # ydl.params['outtmpl']['default'] = tmp_file.name
            ydl.download([song_url])

            with open(tmp_file.name, 'rb') as f:
                song_data = f.read()
                print(f"test: song_data = {song_data}")

    except Exception as e: 
        print(f"Error downloading song: {e}")
        return None