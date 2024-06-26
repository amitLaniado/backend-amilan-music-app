from models import PlaylistCreate, SongPlaylistAdd
from repositories.playlist_repository import create_playlist, get_song_id, create_song, create_playlist_song, get_playlists, get_songs_by_playlist_id, update_songs_amount_by_1

def fetch_playlists(user_id: int):
    playlists = get_playlists(user_id) 
    return playlists

def fetch_songs_by_playlist_id(playlist_id: int):
    songs = get_songs_by_playlist_id(playlist_id)
    return songs

def arrange_create_playlist(playlist: PlaylistCreate):
    return create_playlist(playlist)

def arrange_add_song_to_playlist(songPlaylist: SongPlaylistAdd):
    song_id = get_song_id(songPlaylist.url)
    if song_id is None:
        song_id = create_song(songPlaylist)
    playlist_song_id = create_playlist_song(songPlaylist.playlist_id, song_id)
    update_songs_amount_by_1(songPlaylist.playlist_id)
    return playlist_song_id