from serch_40 import finding_chart
from spotify import connect
from spotify import search_spotify_song
from spotify import spotify_connection
from spotify import connect
from spotify import insert_songs
from spotify import insert_charts
from getting_dates import formated_date
from getting_dates import working_out_date

date = "20200703"
while True:
    date = working_out_date(date)
    app_token = spotify_connection('7d012ee053664c2c8c3b5d3f4394b771','37182ad3df1c431ca9f9fffc13c72c8b')
    databse_connection = connect('pythonsqlite.db')
    website = "https://www.officialcharts.com/charts/uk-top-40-singles-chart/" + date + "/750140/"
    getting_chart = finding_chart(website)
    song_no = 0
    add_date = formated_date(date)
    databse_connection = connect('pythonsqlite.db')
    for  songs in getting_chart[0]:
        try:
            combined_text = ''
            if " FT " in str(getting_chart[2][song_no]):
                split_text_artist = str(getting_chart[2][song_no]).split(' FT ')
                if "/" in split_text_artist:
                    split_text_artist = str(split_text_artist).split('/')
                    for text in split_text_artist:
                        split_text_artist += text + " "
                for text in split_text_artist:
                    combined_text += text + " "
                serch_term = str(getting_chart[1][song_no]) + " " + combined_text
                print(serch_term)

                song = search_spotify_song(app_token, split_text_artist)
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no+1
                insert_charts(databse_connection, chart)
            elif "/" in str(getting_chart[2][song_no]):
                split_text_artist = str(getting_chart[2][song_no]).split('/')
                for text in split_text_artist:
                    combined_text += text + " "
                serch_term = str(getting_chart[1][song_no]) + " " + combined_text
                print(serch_term)

                song = search_spotify_song(app_token, serch_term)
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no+1
                insert_charts(databse_connection, chart)
            elif "&" in str(getting_chart[2][song_no]):
                split_text_artist = str(getting_chart[2][song_no]).split(' & ')
                for text in split_text_artist:
                    combined_text += text + " "
                serch_term = str(getting_chart[1][song_no]) + " " + combined_text
                print(serch_term)

                song = search_spotify_song(app_token, serch_term)
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no + 1
                insert_charts(databse_connection, chart)
            else:
                serch_term = str(getting_chart[1][song_no]) + " " + str(getting_chart[2][song_no])
                print(serch_term)

                song = search_spotify_song(app_token, serch_term)
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no + 1
                insert_charts(databse_connection, chart)
        except:
            try:
                serch_term = str(getting_chart[1][song_no]) + " " + str(getting_chart[2][song_no])
                print(serch_term)

                song = search_spotify_song(app_token, serch_term)
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no + 1
                insert_charts(databse_connection, chart)
            except:
                serch_term = str(getting_chart[1][song_no]) + " " + str(getting_chart[2][song_no])
                song = (serch_term[0:22],'null','null','null','null', 'null','null','null','null','null','null','null','null','null','null','null','null','null')
                print("fuck john legend")
                insert_songs(databse_connection, song)
                chart = add_date, str(song[0]), song_no + 1
                insert_charts(databse_connection, chart)
        song_no = song_no + 1



