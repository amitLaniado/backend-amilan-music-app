from models import PlaylistCreate, SongPlaylist
from repositories.playlist_repository import create_playlist, get_song_id, create_song, create_playlist_song, delete_playlist_song, get_playlists, get_songs_by_playlist_id, update_songs_amount

def fetch_playlists(user_id: int):
    playlists = get_playlists(user_id) 
    return playlists

def fetch_songs_by_playlist_id(playlist_id: int):
    songs = get_songs_by_playlist_id(playlist_id)
    return songs

def arrange_create_playlist(playlist: PlaylistCreate):
    return create_playlist(playlist)

def arrange_create_song_to_playlist(songPlaylist: SongPlaylist):
    song_id = get_song_id(songPlaylist.url)
    if song_id is None:
        song_id = create_song(songPlaylist)
    playlist_song_id = create_playlist_song(songPlaylist.playlist_id, song_id)
    update_songs_amount(songPlaylist.playlist_id, 1)
    return playlist_song_id

def arrange_delete_song_to_playlist(songPlaylist: SongPlaylist):    
    song_id = get_song_id(songPlaylist.url)
    if song_id is None:
        raise Exception("There isn't such song in my db (according the url)")
    playlist_song_id = delete_playlist_song(songPlaylist.playlist_id, song_id)
    update_songs_amount(songPlaylist.playlist_id, -1)
    return playlist_song_id