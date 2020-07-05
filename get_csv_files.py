import sqlite3
from sqlite3 import Error
def connect(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    return (sqliteConnection)
def sql_select(sqliteConnection, select):
    try:
        c = sqliteConnection.cursor()
        c.execute(select)
        myresult = c.fetchall()
        print('data gathered')
    except Error as e:
        print(e)
    return myresult
def csv_creation(headers,csv_file,data):
    import csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([headers])
        writer.writerows(data)

avergae_song_by_week = """SELECT avg(songs.duration_ms)/1000 / 60 as average_song_duration_in_minitues,
avg(songs.valence),
REPLACE(chart.chart_date,'/','-')
FROM songs
INNER JOIN chart
ON songs.song_id = chart.song_id
GROUP BY chart.chart_date
ORDER BY chart.chart_date;"""

avergae_song_by_month = """SELECT avg(songs.duration_ms)/1000 / 60 as average_song_duration_in_minitues,
avg(songs.valence),
REPLACE(strftime('%Y-%m', REPLACE(chart.chart_date,'/','-')),' ','-') as month,
strftime('%Y', REPLACE(chart.chart_date,'/','-')) as year
FROM songs
INNER JOIN chart
ON songs.song_id = chart.song_id
GROUP BY month 
ORDER BY year;"""

avergae_song_by_year = """SELECT avg(songs.duration_ms)/1000 / 60 as average_song_duration_in_minitues,
avg(songs.valence),
strftime('%Y', REPLACE(chart.chart_date,'/','-')) as year
FROM songs
INNER JOIN chart
ON songs.song_id = chart.song_id
GROUP BY year
ORDER BY year"""

def avergae_song_by_month_where_year(year):
    select_statment = """SELECT avg(songs.duration_ms)/1000 / 60 as average_song_duration_in_minitues,
    avg(songs.valence),
    REPLACE(strftime('%m', REPLACE(chart.chart_date,'/','-')),' ','-') as month,
    REPLACE(strftime('%Y-%m', REPLACE(chart.chart_date,'/','-')),' ','-') as month_year,
    strftime('%Y', REPLACE(chart.chart_date,'/','-')) as year
    FROM songs
    INNER JOIN chart
    ON songs.song_id = chart.song_id
    WHERE year = '""" + str(year) + """'
    GROUP BY month_year 
    ORDER BY year;"""

    return select_statment

getting_avergae_song_by_month= """SELECT avg(songs.duration_ms)/1000 / 60 as average_song_duration_in_minitues,
avg(songs.valence),
REPLACE(strftime('%m', REPLACE(chart.chart_date,'/','-')),' ','-') as month
FROM songs
INNER JOIN chart
ON songs.song_id = chart.song_id
GROUP BY month;"""

databse_connection = connect('pythonsqlite.db')

avg_song = sql_select(databse_connection, avergae_song_by_week)
headers1 =  ["average_song_duration_in_minitues", "average_song_valience", "date"]
csv_creation(headers1,"avg_song_len.csv", avg_song)

avg_song_month = sql_select(databse_connection, avergae_song_by_month)
headers2 =  ["average_song_duration_in_minitues", "average_song_valience", "month", "year"]
csv_creation(headers2,"avg_song_len_by_month.csv", avg_song_month)

avergae_song_year = sql_select(databse_connection, avergae_song_by_year)
headers3 =  ["average_song_duration_in_minitues", "average_song_valience", "year"]
csv_creation(headers3,"avg_song_len_by_year.csv", avergae_song_year)

year=2020
while year !=2008:
    avergae_song_month_year = sql_select(databse_connection, avergae_song_by_month_where_year(year))
    headers4 =  ["average_song_duration_in_minitues", "average_song_valience","month","month_year", "year"]
    csv_creation(headers4,"avg_song_len_month_"+str(year)+".csv", avergae_song_month_year)
    year = year-1
average_by_month = sql_select(databse_connection, getting_avergae_song_by_month)
headers5 =  ["average_song_duration_in_minitues", "average_song_valience", "month"]
csv_creation(headers5,"avg_song_len_grouped_by_month.csv", average_by_month)