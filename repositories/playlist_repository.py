from models import PlaylistCreate, SongPlaylist, PlaylistsOut, PlaylistDetails, SongsOut, SongDetails
from database_connection import cursor, connection

# add songs_amount to the playlist

def get_playlists(user_id: int):
    cursor.execute("""
        SELECT id, name, songs_amount FROM "Playlists"
        WHERE user_id=%s
    """, (user_id,))

    playlists = cursor.fetchall() # array of tuple that have playlist_id, playlist_name
    playlists_out = PlaylistsOut(playlists=[PlaylistDetails(playlist_id=row[0], playlist_name=row[1], songs_amount=row[2]) for row in playlists])
    return playlists_out

def get_songs_by_playlist_id(playlist_id: int):
    cursor.execute("""
        SELECT s.name, s.channel, s.url
        FROM "Songs" s
        INNER JOIN "Playlist_Songs" ps ON s.id = ps.song_id
        WHERE ps.playlist_id = %s;
    """, (playlist_id,))

    songs = cursor.fetchall()
    songs_out = SongsOut(songs=[SongDetails(title=song[0], channel=song[1], url=song[2]) for song in songs])
    return songs_out

def create_playlist(playlist: PlaylistCreate):
    try:
        cursor.execute("""
            INSERT INTO "Playlists" (name, user_id)
            VALUES (%s, %s)
            RETURNING id;
        """, (playlist.playlist_name, playlist.user_id))
        connection.commit()

        new_playlist_id = cursor.fetchone()[0]
        return new_playlist_id
    except Exception as e: 
        connection.rollback()
        raise Exception(f"create playlist failed: {e}")

def get_song_id(song_url: str):
    try:
        cursor.execute("""
            SELECT id FROM "Songs"
            WHERE url=%s
        """, (song_url,))
        
        song_id = cursor.fetchone()[0]
        return song_id
    except Exception as e:
        print(f"Failed to get song id: {e}")
        return None


def create_song(SongPlaylist: SongPlaylist):
    try:
        cursor.execute("""
            INSERT INTO "Songs" (name, channel, url)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (SongPlaylist.song_name, SongPlaylist.channel, SongPlaylist.url))
        connection.commit()

        new_song_id = cursor.fetchone()[0]
        return new_song_id
    except Exception as e:
        connection.rollback()
        raise Exception(f"create song failed: {e}")

def create_playlist_song(playlist_id, song_id):
    try:
        cursor.execute("""
            INSERT INTO "Playlist_Songs" (playlist_id, song_id)
            VALUES (%s, %s)
            RETURNING id;
        """, (playlist_id, song_id))
        connection.commit()

        new_playlist_song_id = cursor.fetchone()[0]
        return new_playlist_song_id
    except Exception as e: 
        connection.rollback()
        raise Exception(f"create playlist song failed: {e}")

def delete_playlist_song(playlist_id, song_id):
    try:
        cursor.execute("""
            DELETE FROM "Playlist_Songs" 
            WHERE playlist_id=%s AND song_id=%s
            RETURNING id;
        """, (playlist_id, song_id,))
        connection.commit()

        deleted_playlist_song_id = cursor.fetchone()[0]
        return deleted_playlist_song_id
    except Exception as e: 
        connection.rollback()
        raise Exception(f"deleted playlist song failed: {e}")

def update_songs_amount(playlist_id: int, increase_amount: int):
    try:
        cursor.execute("""
            UPDATE "Playlists"
            SET songs_amount = songs_amount + %s
            WHERE id=%s;
        """, (increase_amount, playlist_id,))
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise Exception(f"update songs amount failed: {e}")
