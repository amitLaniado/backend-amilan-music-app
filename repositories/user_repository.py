from database_connection import cursor, connection
from models import UserRegister, UserLogin, UserOut
from fastapi import HTTPException, status

def register(user: UserRegister):
    try:
        cursor.execute("""
            INSERT INTO "Users" (user_name, hashed_password, email) 
            VALUES (%s, %s, %s)
            RETURNING user_id;
        """, (user.user_name, user.password, user.email))
        connection.commit()

        new_user_id = cursor.fetchone()[0]
        return new_user_id
    except Exception as e:
        # Handle the exception here (e.g., log the error, rollback the transaction)
        connection.rollback()
        raise Exception(f"Registration failed: {e}")
        

def login(user: UserLogin):
    cursor.execute("""
        SELECT user_id FROM "Users" 
        WHERE user_name=%s AND hashed_password=%s;
    """, (user.user_name, user.password))

    try:
        user_id = cursor.fetchone()[0]
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return user_id
