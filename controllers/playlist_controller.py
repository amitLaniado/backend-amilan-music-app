from fastapi import APIRouter, HTTPException, status
from models import PlaylistCreate, SongPlaylistAdd, PlaylistIdentifier, PlaylistsOut, PlaylistDetails, UserIdentifier, SongsOut
from services.playlist_service import arrange_create_playlist, arrange_add_song_to_playlist, fetch_playlists, fetch_songs_by_playlist_id

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
)

# @router.get("/", status_code=status.HTTP_200_OK, response_model=PlaylistsOut)
# def handle_get_playlists(userIdentifier: UserIdentifier):
#     try: 
#         playlists = fetch_playlists(userIdentifier.user_id)
#         return playlists
#     except Exception as e: 
        # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=PlaylistsOut)
def handle_get_playlists(user_id: int):
    try: 
        playlists = fetch_playlists(user_id)
        return playlists
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{playlist_id}", status_code=status.HTTP_200_OK, response_model=SongsOut)
def handle_get_playlist(playlist_id: int):
    try:
        songs = fetch_songs_by_playlist_id(playlist_id)
        return songs
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlaylistIdentifier)
def handle_create_playlist(playlist: PlaylistCreate): 
    try: 
        new_playlist_id = arrange_create_playlist(playlist)
        return { "playlist_id": new_playlist_id }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/song", status_code=status.HTTP_201_CREATED)
def handle_add_song_to_playlist(songPlaylist: SongPlaylistAdd):
    try: 
        new_playlist_song_id = arrange_add_song_to_playlist(songPlaylist)
        return { "playlist_song_id": new_playlist_song_id }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
