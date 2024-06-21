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

class PlaylistCreate(BaseModel):
    playlist_name: str
    user_id: int

class PlaylistOut(BaseModel):
    playlist_id: int
    # playlist_name: str
    # user_id: int