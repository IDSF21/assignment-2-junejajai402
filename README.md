# assignment-2-junejajai402
assignment-2-junejajai402 created by GitHub Classroom
We worked with the spotify dataset since we were interested in a musical dataset. The spotify dataset we found had a rich feature set which was relatable and sufficient for data analysis enabling us to get important analytics from there. Spotify has been around for a long time and has collected some great insights and data as well.\

Goals:\

Our goals were to have good visualization queries and interact with the data to display valuable and important information. We wanted the user to be able to answer a few questions based on the dataset. \
1. What were the top tracks over the 5 years based on number of streams based on artist or genre (top 5/10/15/25)
2. Who were the top artists overall and per genre based on number of streams (top 5/10/15/25)
3. What were the top genres based on number of streams (top 5/10/15/25)
4. Stream evolution over the 5 years for the top 5/10 artists

These questions were important to us as they helped us answer questions about trending artists and genres over time. Seeing the graphs evolve helped us as well see how the people listening to music on the platform has grown over the course of time (in this case over 5 years). As avid music listeners ourselves we found it important to understand what data was collected by spotify about us and what we can glean from seemingly normal datasets.


Rationale: \
1. One of the first choices we made was to limit the maximum number of items displayed to 25 for normal graphs and 10 for the stream evolution. This was because the overall display for more was getting very crowded
2. We limited the stream evolution chart further since the graph is extremely crowded making it harder to see the data.
3. We chose bar graphs over line graphs for the main displays as the information was better suited to being displayed as a bar graph. Other graphs were a bit confusing.
4. We chose a line graph for the stream evolution since we felt that line charts would better showcase the comparisons between different artists.
5. We made some of the interactions in having choices for whether the aggregation should be via artist or by genre. We were considering position in the billboard top 200 which is a column in the data and by trackName but ultimately thought that they were either too granular or didnt provide enough interesting visualizations.

Overview of development:
  -> We first cleaned the data set (Jaideep) \
  -> Then we explored the data and decided to ask questions based on observed features and data (Jaideep and Keertana) \
  -> We then queried the dataset for the columns we needed (Jaideep) \
  -> We then built interactive data elements in streamlit (Keertana) \ 
