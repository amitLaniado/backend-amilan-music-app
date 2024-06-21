from models import PlaylistCreate
from database_connection import cursor, connection

async def create_playlist(playlist: PlaylistCreate):
    try:
        cursor.execute("""
            INSERT INTO "Playlist" (playlist_name, user_id)
            VALUES (%s, %s)
            RETURNING playlist_id;
        """, (playlist.playlist_name, playlist.user_id))
        connection.commit()

        new_playlist_id = cursor.fetchone()[0]
        return new_playlist_id
    except Exception as e: 
        connection.rollback()
        raise Exception(f"create playlist failed: {e}")
