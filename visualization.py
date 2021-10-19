import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)
from urllib.error import URLError

@st.cache(allow_output_mutation=True)
def get_song_data():
    dataset = "cleanData_spotify.csv"
    nRowsRead = None                                                #specify 'None' if want to read whole file
    df1 = pd.read_csv(dataset)
    return df1

try:
    df = get_song_data()
    nRow, nCol = df.shape
    df.dropna(inplace=True)
    if type(df['Genre'][1]) == str:
        df['Genre'] = df['Genre'].apply(lambda x: ast.literal_eval(x))
    df2 = df.explode('Genre')
    
    actions = ["Select Action", "Top Tracks being Played", "Top Favorite Artists", "Most Loved Genres", "Compare Stream Evolution of Artists"]
    actionToDo = st.sidebar.selectbox('Explore the data!', actions)

    streams = str(df['Streams'].sum(axis=0))
    if actionToDo == "Select Action":
        st.title("Welcome to the Spotify Data Analytics Dashboard!")

        
        st.metric("Total Streams since 2017", streams, delta="Constantly Increasing!!", delta_color='normal')

        st.info("This dashboard was developed by Keertana Kamesh and Jaideep Juneja as a group for Homework 2 on the Interactive Data Science Course. \
        Spotify is the largest on-demand music service and uses big data for running machine learning techniques to deliver a unique and personalized music listening experience. \
        Being music-lovers and everyday users of the app, we chose to work on this dataset because of how relatable it was and to explore how the features are used to provide a personalized user experience to a listener. \
        Click on the side-bar to explore the data!")

    else:
        st.title(actionToDo)

    if actionToDo == "Top Tracks being Played":
        col1, col2 = st.columns(2)
        filterChoice = col1.radio('Select Genre/Artist', ['Genre', 'Artist'])
        filterElem = col2.radio('Select number of tracks', ['Top 5', 'Top 10', 'Top 25'])
        noTracks = int(filterElem.split()[-1])
        
        if filterChoice == 'Genre':

            genre = np.concatenate((['-'], df2['Genre'].drop_duplicates()), axis = 0) #change this to genres
            genre_choice = st.selectbox('Select Genre', genre)
            
            dat = df2\
            .query("(Genre == @genre_choice)")\
            .groupby(["Track Name"], as_index = False)\
            .agg(TotalStreams = ("Streams", "sum"))

            st.write("\n\n")
            printData = dat.sort_values('TotalStreams', ascending=False).drop_duplicates('Track Name').head(noTracks)

            fig = px.bar(printData, y='Track Name', x='TotalStreams', text='TotalStreams', color = 'TotalStreams', width=1000, height=500)
            fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            fig.update_layout(yaxis=dict(autorange="reversed"))
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

            table = go.Figure(data=go.Table(columnwidth = [3,2], header=dict(fill_color = "#92959E", values=list(printData.columns), align="center"), cells=dict(values=[printData["Track Name"], printData["TotalStreams"]], height=30)))
            table.update_traces(cells_font=dict(size = 18))
            table.update_layout(width=1000, margin = dict(l=0, r=0, b=0, t=0), font=dict(size=18))
            st.write(table)
            

        if filterChoice == 'Artist':
            artists = np.concatenate((['-'],df['Artist'].drop_duplicates()), axis = 0)
            artist_choice = st.selectbox('Select Artist', artists)
            data = df\
            .query("(Artist == @artist_choice)")\
            .groupby(["Track Name"], as_index = False)\
            .agg(TotalStreams = ("Streams", "sum"))

            st.write("\n\n")
            printData = data.sort_values('TotalStreams', ascending=False).drop_duplicates('Track Name').head(noTracks)

            fig = px.bar(printData, y='Track Name', x='TotalStreams', text='TotalStreams', color = 'TotalStreams', width=1000, height=500)
            fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            fig.update_layout(yaxis=dict(autorange="reversed"))
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

            table = go.Figure(data=go.Table(columnwidth = [3,2], header=dict(fill_color = "#92959E", values=list(printData.columns), align="center"), cells=dict(values=[printData["Track Name"], printData["TotalStreams"]], height=30)))
            table.update_traces(cells_font=dict(size = 18))
            table.update_layout(width=1000, margin = dict(l=0, r=0, b=0, t=0), font=dict(size=18))
            st.write(table)
    
    if actionToDo == "Top Favorite Artists":
        filterChoice = st.radio('Select number of Artists', ['Top 5', 'Top 10', 'Top 25'])        
        intChoice = int(filterChoice.split()[-1])

        topArtists = df\
        .groupby(["Artist"], as_index = False)\
        .agg(TotalStreams = ("Streams", "sum"))\
        .sort_values('TotalStreams', ascending=False)
        
        topArtists1 = topArtists.head(intChoice)   #get artists from dataframe
        artists = topArtists1['Artist'].tolist()

        fig = px.bar(topArtists1, y='Artist', x='TotalStreams', text='TotalStreams', color = 'TotalStreams', width=1000, height=500)
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(yaxis=dict(autorange="reversed"))
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

        for a in artists:
            top = st.expander(a, False)
            tracks = df\
            .query("(Artist == @a)")\
            .groupby(["Track Name"], as_index = False)\
            .agg(TotalStreams = ("Streams", "sum"))
            top.write("Top Tracks by {}".format(a))
            tracks1 = tracks.sort_values('TotalStreams', ascending=False).drop_duplicates('Track Name').head(3)
            tracks2 = tracks1["Track Name"].tolist()
            for t in tracks2:
                top.write(t)

        #add a bar graph with artists vs. total streams or pie chart with artists and percentage genre

    if actionToDo == "Most Loved Genres":
        #filterChoice = st.radio('Select Genre/Artist', ['Genre', 'Artist'])
        filterChoice = st.radio('Select number of Genres', ['Top 5', 'Top 10', 'Top 25'])        
        intChoice1 = int(filterChoice.split()[-1])

        topGenres = df2\
        .groupby(["Genre"], as_index = False)\
        .agg(TotalStreams = ("Streams", "sum"))\
        .sort_values('TotalStreams', ascending=False)

        topGenres1 = topGenres.head(intChoice1)   #get artists from dataframe
        genres = topGenres1['Genre'].tolist()

        fig = px.bar(topGenres1, y='Genre', x='TotalStreams', text='TotalStreams', color = 'TotalStreams', width=1000, height=500)
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(yaxis=dict(autorange="reversed"))
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

        for g in genres:
            top = st.expander(g, False)
            tracks = df2\
            .query("(Genre == @g)")\
            .groupby(["Track Name"], as_index = False)\
            .agg(TotalStreams = ("Streams", "sum"))
            top.write("Top Tracks in {}".format(g))
            tracks1 = tracks.sort_values('TotalStreams', ascending=False).drop_duplicates('Track Name').head(3)
            tracks2 = tracks1["Track Name"].tolist()
            for t in tracks2:
                top.write(t)

    if actionToDo == "Compare Stream Evolution of Artists":

        numberArtists = st.select_slider( 'Select number of Artists', options=['1', '2', '3', '4', '5'])
        number = int(numberArtists)

        if number <= 1:
            st.error("Select atleast 2 artists to compare")
        else:
            artistsSelected = st.multiselect("Choose Artists", list(df['Artist'].drop_duplicates()), ["Ariana Grande", "Justin Bieber"])

            if not artistsSelected:
                st.error("Please select atleast {} artist.".format(number))
            if len(artistsSelected) != number:
                st.error("Select only {} artists".format(number))            
            
            else:

                df7 = df[df['Artist'].isin(artistsSelected)]
                top5Artists = df7\
                .groupby(["Artist"], as_index = False)\
                .agg(TotalStreams = ("Streams", "sum"))\
                .sort_values('TotalStreams', ascending=False)

                top5Artists = top5Artists.Artist
                
                TotalStreamsTop5 = df7\
                .groupby(["Year","Artist"], as_index = False)\
                .agg(TotalStreams = ("Streams", "sum"))

                fig = go.Figure()
                for artist in TotalStreamsTop5.Artist.unique():
                    artist_data = TotalStreamsTop5.query("(Artist == @artist)").groupby(["Year","Artist"], as_index = False).agg(TotalStreams = ("TotalStreams", "sum"))
                    fig.add_trace(go.Scatter(x=artist_data['Year'], y=artist_data['TotalStreams'], name=artist))

                fig.update_layout(xaxis_title="Date", yaxis_title="Streams", title="Cumulative Streams Evolution of Selected Artists", width=1000, height=500)
                st.plotly_chart(fig)
    
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
        """
        % e.reason
    )