from fastapi import APIRouter, Response
# from fastapi.responses import StreamingResponse
from services.song_service import fetch_song

router = APIRouter(
    prefix="/song",
    tags=["song"],
)

@router.get("/{song_name}")
async def handle_song(song_name):
    song_data = await fetch_song(song_name)

    if song_data:    
        headers = {
            "Content-Type": "audio/mpeg",
            "Content-Disposition": "attachment; filename=song.mp3"
        }
        return Response(content=song_data, headers=headers) 
    else:
        return Response(content="There are no results to this search", status_code=404)