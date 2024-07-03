from database_connection import cursor, connection
from models import UserRegister, UserLogin, UserOut, PlaylistCreate
from fastapi import HTTPException, status
from .playlist_repository import create_playlist

def register(user: UserRegister):
    try:
        cursor.execute("""
            INSERT INTO "Users" (name, hashed_password, email) 
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (user.user_name, user.password, user.email))
        connection.commit()

        new_user_id = cursor.fetchone()[0]
        create_playlist(PlaylistCreate(playlist_name="liked music", user_id=new_user_id))
        return new_user_id
    except Exception as e:
        # Handle the exception here (e.g., log the error, rollback the transaction)
        connection.rollback()
        raise Exception(f"Registration failed: {e}")

def login(user: UserLogin):
    cursor.execute("""
        SELECT id FROM "Users" 
        WHERE name=%s AND hashed_password=%s;
    """, (user.user_name, user.password))

    try:
        user_id = cursor.fetchone()[0]
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return user_id
