ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f"songs_downloaded/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
