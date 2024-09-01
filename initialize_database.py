from database_connection import cursor, connection

# SQL statements to create the required tables
create_user_table_sql = '''
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    userName VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    hashed_password CHAR(40) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

create_playlists_table_sql = '''
CREATE TABLE IF NOT EXISTS Playlists (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    songs_amount 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

create_playlist_songs_table_sql = '''
CREATE TABLE IF NOT EXISTS PlaylistSongs (
    id SERIAL PRIMARY KEY,
    playlist_id INT REFERENCES Playlists(id) ON DELETE CASCADE,
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

create_songs_table_sql = '''
CREATE TABLE IF NOT EXISTS Songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist VARCHAR(100) NOT NULL,
    album VARCHAR(100),
    released_at DATE
);
'''

def is_table_exist(table_name):
    try:
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM pg_tables
                WHERE schemaname = 'public' AND tablename = %s
            );
        """, (table_name,))
        print("is table exist result: ", cursor.fetchall())
        return cursor.fetchone()[0]
    except Exception as error:
        print(f"Error checking if table exists: {error}")
        return False

def create_table(create_table_sql):
    try:
        cursor.execute(create_table_sql)
        connection.commit()
        print("Table created successfully.")
    except Exception as error:
        print(f"Error creating table: {error}")

def handle_initialize_tables():
    tables = {
        'Users': create_user_table_sql,
        'Playlists': create_playlists_table_sql,
        'PlaylistSongs': create_playlist_songs_table_sql,
        'Songs': create_songs_table_sql
    }

    for table_name, create_table_sql in tables.items():
        if not is_table_exist(table_name):
            print(f"Table '{table_name}' does not exist. Creating...")
            create_table(create_table_sql)
        else:
            print(f"Table '{table_name}' already exists.")

# Initialize tables
handle_initialize_tables()

# # Close the cursor and connection after initializing the tables
# cursor.close()
# connection.close()
