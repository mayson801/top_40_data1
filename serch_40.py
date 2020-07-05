import requests
import csv
from csv import writer


def finding_chart(movie_name):
    i = 0
    chart_pos = []
    artists = []
    songs = []
    website = requests.get(movie_name).text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(website, 'lxml')
    find_table = soup.find("table",{"class": "chart-positions"})
    find_track = find_table.find_all("div",{'class': "title"})
    find_artist = find_table.find_all("div",{'class': "artist"})
    while i != 40:
        format_track_length = len(find_track[i].text)-1
        format_artist_length = len(find_artist[i].text)-1
        #print(str(i+1) + " " + find_track[i].text[1:format_track_length] + " by " + find_artist[i].text[1:format_artist_length])
        chart_pos.append(i+1)
        artists.append(find_artist[i].text[1:format_artist_length])
        songs.append(find_track[i].text[1:format_track_length])
        i = i + 1

    return chart_pos, songs, artists


#actors_href = finding_chart("https://www.officialcharts.com/charts/uk-top-40-singles-chart")
#print(actors_href[1][0])
