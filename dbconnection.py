import sqlite3
from sqlite3 import Error
def connect(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    return (sqliteConnection)

def create_table(sqliteConnection, create_table_sql):
    try:
        c = sqliteConnection.cursor()
        c.execute(create_table_sql)
        print('table_added')
    except Error as e:
        print(e)

sql_create_artist_table = """ CREATE TABLE IF NOT EXISTS artist (
                                    artist_id text PRIMARY KEY,
                                    artist_name text,
                                    artist_DOB DATE
                                    ); """

sql_create_album_table = """ CREATE TABLE IF NOT EXISTS album (
                                        album_id text PRIMARY KEY,
                                        artist_id text,
                                        album_name text,
                                        album_track_nos BIT,
                                        album_len INT, 
                                        album_label text,
                                        album_release_date DATE,
                                        FOREIGN KEY (artist_id)
                                            REFERENCES artist (artist_id)    
                                    ); """


sql_create_song_table = """ CREATE TABLE IF NOT EXISTS songs (
                                        song_id text PRIMARY KEY,
                                        album_id text,
                                        artist_id text,
                                        name text NOT NULL,
                                        track_no BIT,
                                        acousticness FLOAT NOT NULL,
                                        danceability FLOAT NOT NULL,
                                        duration_ms FLOAT NOT NULL,
                                        energy FLOAT NOT NULL,
                                        instrumentalness FLOAT NOT NULL,
                                        key BIT NOT NULL,
                                        liveness FLOAT NOT NULL,
                                        loudness FLOAT NOT NULL,
                                        mode FLOAT NOT NULL,
                                        speechiness FLOAT NOT NULL,
                                        tempo FLOAT NOT NULL,
                                        time_signature FLOAT NOT NULL,
                                        valence FLOAT NOT NULL,
                                        FOREIGN KEY (artist_id)
                                            REFERENCES artist (artist_id)
                                        FOREIGN KEY (album_id)
                                            REFERENCES album (album_id)  
                                    ); """

sql_create_chart_table = """    CREATE TABLE IF NOT EXISTS chart (
                                chart_date Date,   
                                song_id text,
                                chart_pos BIT,
                                FOREIGN KEY (song_id)
                                    REFERENCES songs (song_id)
                                PRIMARY KEY (chart_date, song_id)
                                    ); """

databse_connection = connect('pythonsqlite.db')
#create_table(databse_connection, sql_create_song_table)
create_table(databse_connection, sql_create_artist_table)
create_table(databse_connection, sql_create_album_table)
create_table(databse_connection, sql_create_song_table)
create_table(databse_connection, sql_create_chart_table)


