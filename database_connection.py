import psycopg2
import os
# from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}
print(f"db_params = {db_params}")

# database_url = "postgresql://postgres:amit2008@localhost/amilan_music_app"

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)

    # connection = psycopg2.connect(database_url)
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
