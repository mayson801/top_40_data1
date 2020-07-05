import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


main_df1 = pd.read_csv('avg_song_len.csv')
fig1 = px.line(main_df1, x="date", y="average_song_duration_in_minitues")

main_df2 = pd.read_csv('avg_song_len_by_month.csv')
main_df3 = pd.read_csv('avg_song_len_by_year.csv')
fig2 = go.Figure()
fig2.update_layout(
    legend_orientation="h",
)
fig2.add_trace(go.Scatter(x = main_df2['month'], y = main_df2['average_song_duration_in_minitues'], name='avg song lenghth month'))
fig2.add_trace(go.Scatter(x = main_df3['year'], y = main_df3['average_song_duration_in_minitues'], name='avg song lenghth by year'))

df4 = pd.read_csv('avg_song_len_by_no1.csv')
df3_1 = pd.read_csv('avg_song_len_by_month_no1.csv')
df3_2 = pd.read_csv('avg_song_len_by_year_no1.csv')
fig3 = go.Figure()
fig3.update_layout(
    legend_orientation="h",
)
fig3.add_trace(go.Scatter(x = df4[' date'], y = df4['average_song_duration_in_minitues'], name='avg song lenghth_no1'))
fig3.add_trace(go.Scatter(x = df3_1[' month'], y = df3_1['average_song_duration_in_minitues'],name='avg song lenghth month_no1'))
fig3.add_trace(go.Scatter(x = df3_2[' year'], y = df3_2['average_song_duration_in_minitues'],name='avg song lenghth by year_no1'))

fig4 = go.Figure()
fig4.update_layout(
    legend_orientation="h",
)
fig4.add_trace(go.Scatter(x=main_df1['date'], y=main_df1['average_song_valience'], name='avg song valence month'))
fig4.add_trace(go.Scatter(x = main_df2['month'], y = main_df2['average_song_valience'], name='avg song valence month'))
fig4.add_trace(go.Scatter(x = main_df3['year'], y = main_df3['average_song_valience'], name='avg song valence by year'))

fig5 = go.Figure()
fig5.update_layout(
    legend_orientation="h",
)
year=2020
while year != 2008:
    monthcsv = pd.read_csv('avg_song_len_month_'+str(year)+'.csv')
    fig5.add_trace(go.Scatter(x=monthcsv['month'], y=monthcsv['average_song_valience'], name=str(year)))
    year=year-1
monthcsv = pd.read_csv('avg_song_len_grouped_by_month.csv')
fig5.add_trace(go.Scatter(x=monthcsv['month'], y=monthcsv['average_song_valience'], name='10 year average'))


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
section1 = html.Div(className='content', children=[
        html.P('This data was gathered from the officialcharts uk-top-40-singles-chart and has every song on the top 40 and the chart position in the last 10 years.This was accomalished using python and the web scraping package Beautiful Soup.The song name and artist is then passed spotify web API to find out meta data about the song such as song duration,BPM,ECT.The data however is not 100% accurate as the name and artist from the offical chart does not match the name and artist,this has led to a few covers being added rather than the actual song and there are also 52 songs that can not be found at all. Iam trying to manually fix these however it takes time'),
        dcc.Graph(
            id='AVG_song_len',
            figure=fig1
        ),
        html.P('As you can see from the graph above you can see a very obvious decline in the average lenghth of songs.The decresses is even sharper if you look at the average song lenght of the year or average song lenght of the month by month as shown below.Streaming is likly the cause as Charlie Harding writer fot the verge explains'),

        html.Table(children=[
            html.Tr(children=[
            html.Td(dcc.Graph(
                id='AVG_song_len_month_year',
                figure=fig2
            ),style={'width': '49%', 'display': 'inline-block'}),
            html.Td('"One of the main things that has changed is how people are getting paid, and it’s is affecting how songs are being written. In the past, you used to get paid if you sold an album or a single. In 1995, we had songs that were coming in at four minutes and 30 seconds. Today, songs are down to three minutes and 42 seconds, because of the difference in how artists are getting paid now. Instead of getting paid by physical sales, you’re getting paid in a stream, which only counts if someone listens to 30 seconds of a song. It actually makes sense if you can have more songs streamed at a time, which means that you want to pack your album full of much shorter songs. So if you have an album like Drake’s Scorpion, which is a really long double album coming in at almost 90 minutes, he’s got a ton of really short songs on there, because he gets paid for every song you listen to, whether or not you listen to the whole album."[1]',
                    style={'width': '39%', 'display': 'inline-block',}),
            ]),
        ]),

        html.Table(children=[
            html.Tr(children=[
            html.Td(dcc.Graph(
                id='life-exp-vs-gdp',
                figure=fig3
            ),style={'width': '49%', 'display': 'inline-block'}),
            html.Td('it is not all doom and gloom for fans of longer songs as the average length of the number 1 song has stayed pretty stable escpecially when looking at yearly averages it has shows little patten of trending down however in the last 3 years there is defentialy a downward trend. ',style={'width': '39%', 'display': 'inline-block',}),
            ]),
        ]),
    ])
section2 = html.Div(className='content', children=[
    dcc.Graph(
        id='Song valence',
        figure=fig4
    ),
        html.P('spotfy defines a song based on valence which they explain "Describes the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)."[2]'),
        html.P('As you can see from the graph above you can see a very obvious decline in the average lenghth of songs.The decresses is even sharper if you look at the average song lenght of the year or average song lenght of the month by month as shown below.Streaming is likly the cause as Charlie Harding writer fot the verge explains'),
    html.Table(children=[
        html.Tr(children=[
            html.Td(dcc.Graph(
                id='AVG_song_len_month',
                figure=fig5
            ), style={'width': '49%', 'display': 'inline-block'}),
            html.Td(
                'it is not all doom and gloom for fans of longer songs as the average length of the number 1 song has stayed pretty stable escpecially when looking at yearly averages it has shows little patten of trending down however in the last 3 years there is defentialy a downward trend.',
                style={'width': '39%', 'display': 'inline-block', }),
        ]),
    ]),

    ])

def make_item(i,title,string):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"{title}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(string),
                id=f"collapse-{i}",
            ),
        ]
    )


accordion = html.Div(
    [make_item(1,'how streaming has changed music--looking at music length over the last 10 years',section1), make_item(2,'happiness in music through the years',section2), make_item(3,'section_3',html.P('help')), make_item(4,'section_4',html.P('help'))], className="accordion"
)
app.layout = html.Div(children=[
    html.H4('A Look At Pop Music In The Last 10 Years'),
    accordion,
html.Div(children=[
html.P('https://www.theverge.com/2019/5/28/18642978/music-streaming-spotify-song-length-distribution-production-switched-on-pop-vergecast-interview'),
html.P('https://towardsdatascience.com/what-makes-a-song-likeable-dbfdb7abe404')
])
])
@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 5)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 5)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 5)],
)
def toggle_accordion(n1, n2, n3, n4, is_open1, is_open2, is_open3, is_open4):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False, False, False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3, False
    elif button_id == "group-4-toggle" and n4:
        return False, False, False, not is_open4
    return False, False, False, False

if __name__ == '__main__':
    app.run_server(debug=True)
