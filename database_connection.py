import psycopg2
from psycopg2 import sql

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "amilan_music_app"
user = "postgres"
password = "amit2008"

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    print("Connected to the database successfully.")
    
except Exception as error:
    print(f"Error connecting to the database: {error}")

# async def get_users():
#     select_query = 'SELECT * FROM "Users"'
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     return rows

# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed.")
