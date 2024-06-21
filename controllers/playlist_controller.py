from fastapi import APIRouter, HTTPException, status
from models import PlaylistCreate, PlaylistOut
from services.playlist_service import arrange_create_playlist

router = APIRouter(
    prefix="/playlist",
    tags=["playlist"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlaylistOut)
async def handle_create_playlist(playlist: PlaylistCreate): 
    try: 
        new_playlist_id = await arrange_create_playlist(playlist)
        return { "playlist_id": new_playlist_id }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# @router.post("/song", status_code=status.HTTP_201_CREATED)