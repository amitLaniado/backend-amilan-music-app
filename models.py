from typing import List
from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    user_name: str
    password: str

class UserOut(BaseModel):
    user_id: int
    # user_name: str
    # email: EmailStr

class UserIdentifier(BaseModel): 
    user_id: int

class SongDetails(BaseModel):
    # song_name: str
    title: str
    channel: str
    url: str

class SongsOut(BaseModel):
    songs: List[SongDetails]

class PlaylistDetails(BaseModel):
    playlist_id: int
    playlist_name: str
    songs_amount: int

class PlaylistsOut(BaseModel):
    playlists: List[PlaylistDetails]

class PlaylistCreate(BaseModel):
    playlist_name: str
    user_id: int

class PlaylistIdentifier(BaseModel):
    playlist_id: int
    # playlist_name: str
    # user_id: int

class SongPlaylistAdd(BaseModel): 
    song_name: str
    channel: str
    url: str
    playlist_id: int