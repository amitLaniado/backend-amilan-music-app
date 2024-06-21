from models import PlaylistCreate
from repositories.playlist_repository import create_playlist

async def arrange_create_playlist(playlist: PlaylistCreate):
    return await create_playlist(playlist)
