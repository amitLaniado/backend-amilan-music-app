from fastapi import APIRouter
from services.song_service import fetch_song

router = APIRouter(
    prefix="/song",
    tags=["song"],
)

@router.get("/{song_name}")
async def handle_song(song_name):
    return await fetch_song(song_name)
