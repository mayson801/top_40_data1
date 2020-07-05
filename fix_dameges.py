import sqlite3
from spotify import search_spotify_song
from spotify import spotify_connection

def connect(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    return (sqliteConnection)
def insert_songs(sqliteConnection, data_tuple):
        cursor = sqliteConnection.cursor()
        sql = ''' UPDATE tasks
                  SET priority = ? ,
                      begin_date = ? ,
                      end_date = ?
                  WHERE id = ?'''
        sql = '''update songs 
                set song_id = ? 
                where 
                    song_id = ?
                     ;'''
        cursor.execute(sql, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")


app_token = spotify_connection('7d012ee053664c2c8c3b5d3f4394b771','37182ad3df1c431ca9f9fffc13c72c8b')
update_data = ('HAPPY CHRISTMAS (WAR I','plz')
serch_term = 'you are not alone x factor finalists 2009'

song = search_spotify_song(app_token, serch_term)
print(song)
databse_connection = connect('pythonsqlite.db')
insert_songs(databse_connection, update_data)

