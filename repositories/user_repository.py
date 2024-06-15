from database_connection import cursor, connection
from models import UserRegister, UserLogin, UserOut

def register(user: UserRegister):
    try:
        cursor.execute('INSERT INTO "Users" (user_name, hashed_password, email) VALUES (%s, %s, %s)', (user.user_name, user.password, user.email))
        connection.commit()
    except Exception as e:
        # Handle the exception here (e.g., log the error, rollback the transaction)
        connection.rollback()
        raise Exception(f"Registration failed: {e}")
        

def login(user: UserLogin):
    cursor.execute("""
        SELECT user_name, email FROM "Users" 
        WHERE user_name=%s AND hashed_password=%s;
    """, (user.user_name, user.password))
    result_user = cursor.fetchone()
    if not result_user:
        return None 
    return { "user_name": result_user[0], "email": result_user[1] } 

