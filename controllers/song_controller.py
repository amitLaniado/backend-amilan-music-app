from fastapi import APIRouter, Response
# from fastapi.responses import StreamingResponse
from services.download_song_service import fetch_download_song
from services.song_options_service import fetch_song_options
from typing import Optional 

router = APIRouter(
    prefix="/song",
    tags=["song"],
)

@router.get("/download")
async def handle_song(song_url: Optional[str] = ''):
    print("song_url: ", song_url)
    song_data = await fetch_download_song(song_url)

    if song_data:    
        headers = {
            "Content-Type": "audio/mpeg",
            "Content-Disposition": "attachment; filename=song.mp3"
        }
        return Response(content=song_data, headers=headers) 
    else:
        return Response(content="There are no results to this search", status_code=404)

@router.get("/songOptions/{song_name}")
async def handle_song_options(song_name):
    song_options = await fetch_song_options(song_name)
    return song_options