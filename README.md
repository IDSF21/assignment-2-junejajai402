# assignment-2-junejajai402
assignment-2-junejajai402 created by GitHub Classroom


Spotify is the largest on-demand music service and uses big data for running machine learning techniques to deliver a unique and personalized music listening experience. Being music-lovers and everyday users of the app, we chose to work on this dataset because of how relatable it was and to explore the features used to provide a customized user experience to a listener. The dataset we found had data of tracks from 2017 to 2021 and had a rich feature set which was sufficient for data analysis enabling us to get important analytics from there.

**Goals:**

Our goals were to have some good visualization queries and interact with the data to display valuable and important information. We wanted the user to be able to answer a few questions based on the dataset. The questions we came up with were - 

1. What were the top tracks over the 5 years based on number of streams giving the user the option to filter based on artist or genre (top 5/10/25)
2. Who were the top artists over the 5 years (top 5/10/25)
3. What were the top genres based on number of streams (top 5/10/25)
4. How the streams have evolved over the 5 years for the top 5 artists
5. Compare how the streams have evolved over the 5 years for some chosen artists

These questions were important to us as they helped us answer questions about trending artists and genres over time. Seeing the graphs evolve helps understand how an artist gains popularity in some year because of a certain track that went viral and how their streams start increasing or decreasing over time. As avid music listeners ourselves we found it important to understand what data was collected by spotify about us and what we can glean from seemingly normal datasets.

**Rationale:** 

1. One of our first choices was to decide the type of graphs to use for our visualizations. Since we were choosing tracks, artists and genres and gauging their popularity based on the number of streams, we chose to go with bar graphs. This was because it was easier for a user to look at the length and colours of the bars and understand the popularity of tracks relative to each other. 
2. The next decision was about how much data did we want on these visualizations. We realized just showing the top 5 tracks aor top 5 artists would restrict the user from a lot  of information. Thus, we decided to have options of looking at 5, 10 or 25 datapoints. We decided to limit the maximum number of items displayed to 25 for the graphs as beyond this, the graphs were getting too cluttery which would again lead to the user not wanting to look at the information.
3. Next, we worked on the visualization to show the evolutions of streams for artists and also allow the user to compare the stream evolutions of artists of their choice. We decided to go with line charts for this as it was less cluttery and allowed for better comparison between the artists streams. Here, we limited to having upto 5 artists on these charts as again, too many lines seemed confusing to locate the lines for the artists.
4. We made some of the interactions in having choices for whether the aggregation should be via artist or by genre. While showing the top artists and genres, we also created some expanders to display the 3 most popular tracks of that artist or genre. We were considering to use the position in the billboard top 200 which is a column in the dataset to make some decisions about popularity of tracks but ultimately thought that they were either too granular or didnt provide enough interesting visualizations.

**Overview of development:**

After choosing the dataset for the assignment, we first sat down together to think of some interesting questions that the dataset could answer, and explored the features. After coming to a conclusion about some of the questions and creating a layout of how we wanted the dashboard to look like and the visualizations that we wanted on it, Jaideep worked on cleaning the dataset, and writing the Pandas queries to get the required data for the visualizations on the dashboard. Next step was to plan out the dashboard on Streamlit, get all the visualizations working and have the visualizations respond to all the interactive elements on the dashboard. Keertana worked on the the dashboard and built all these interactions using Streamlit and Plotly for the graphs. We then worked on creating this file with all the details of our assignment together. 

**Components of the Assignment**

data.csv - Spotify dataset taken from Kaggle - https://www.kaggle.com/tawejssh/spotify-dataset-eda-insights/data

dataCleaningAndExplortion.ipynb - Jupyter Notebook with the steps used to clean the dataset for further exploration and data analysis. Some of the steps for cleaning and visualization were inspired from this notebook - https://www.kaggle.com/tawejssh/spotify-dataset-eda-insights/notebook

cleanData_spotify.csv - The dataset obtained after cleaning

visualization.py - The Python code that uses streamlit and plotly for the dashboard.
