import tekore as tk
import sqlite3
from sqlite3 import Error


def connect(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    return (sqliteConnection)


def insert_songs(sqliteConnection,data_tuple):
    try:
        cursor = sqliteConnection.cursor()
        sql = '''INSERT INTO songs(song_id,album_id,artist_id,name,track_no, acousticness,danceability,duration_ms,energy,instrumentalness,key,liveness,loudness,mode,speechiness,tempo,time_signature,valence)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        cursor.execute(sql, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
    except:
        print("song already in datebase")


def insert_charts(sqliteConnection,data_tuple):
    try:
        cursor = sqliteConnection.cursor()
        sql = '''INSERT INTO chart(chart_date,song_id,chart_pos)
                  VALUES(?,?,?);'''
        cursor.execute(sql, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
    except:
        print("UNIQUE constraint failed")


def spotify_connection(client_id,client_secret):
    client_id = client_id
    client_secret = client_secret
    app_token = tk.request_client_token(client_id, client_secret)
    return app_token


def song_album_data(app_token,album_name,connection):
    spotify = tk.Spotify(app_token)
    albums, = spotify.search('kendrick lamar to pimp a butterfly',types=('album',), limit=1)
    album = albums.items[0]
    spotify = tk.Spotify(app_token)
    album = spotify.album(album.id)
    for track in album.tracks.items:
        track_uri_length = len(track.uri)
        track_uri = track.uri[14:track_uri_length]
        track_info = spotify.track_audio_features(track_uri)
        data_tuple = (track_info.id,album.id,'null', track.name,track.track_number, track_info.acousticness, track_info.danceability, track_info.duration_ms, track_info.energy, track_info.instrumentalness, track_info.key, track_info.liveness, track_info.loudness, track_info.mode, track_info.speechiness, track_info.tempo, track_info.time_signature, track_info.valence)
        insert_songs(connection,data_tuple)


def search_spotify_song(app_token,song):
    spotify = tk.Spotify(app_token)
    songs, = spotify.search(song,types=('track',), limit=1)
    song = songs.items[0]
    track_info = spotify.track_audio_features(song.id)

    data_tuple = (
    track_info.id, 'null',song.artists[0].id, song.name,'null', track_info.acousticness, track_info.danceability,
    track_info.duration_ms, track_info.energy, track_info.instrumentalness, track_info.key, track_info.liveness,
    track_info.loudness, track_info.mode, track_info.speechiness, track_info.tempo, track_info.time_signature,
    track_info.valence)

    return  data_tuple

#databse_connection = connect('pythonsqlite.db')
#app_token = spotify_connection('7d012ee053664c2c8c3b5d3f4394b771','37182ad3df1c431ca9f9fffc13c72c8b')

#song = search_spotify_song(app_token, 'kendrick lamar alright')
#print(song)

#chart = " 26/06/2020 ", str(song[0]) , 1
#insert_charts(databse_connection, chart)

