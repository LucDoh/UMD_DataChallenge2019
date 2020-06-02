# mBike Bikeshare Analysis  
## [Best in Community Integration at UMD's 2019 Data Challenge](https://datachallenge.ischool.umd.edu/data-challenge-2019/)

I participated in University of Maryland's 1-week data challenge with a team of 3 other students (Linda, Grace & Ruthwick), where we won Best Community Integration. This repository contains the Jupyter notebooks I used to clean and transform the data, perform EDA to answer our research questions, and make geospatial + statistical visualizations. It also contains our presentation as a pdf.

We performed a combination of temporal and spatial analyses to make recommendations to Zagster on how to improve their bike-share service in College Park, Maryland. By analyzing the bike usage by station and making use of the 1/4 mile standard (an urban planning standard for how far people are willing to walk to a transit station), we predicted the three best new locations for stations. Additionally, we demonstrated how the issue of bike imbalance emerges due the users' tendencies, and showed quantitatively how often trucks would need to balance the stations. Linda & Grace showed how usage varies seaonally, by day of the week as well as with the weather (rain and temperature, from NOAA data).

The tools I used most were:
  * Jupyter Notebooks (Python)
  * Pandas
  * Seaborn
  * Folium

The team used Tableau and SAS.
  
_____________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________

The dataset was provided by the City of College Park with the following information:

### City of College Park mBike Bikeshare Dataset
"Data is from 6/14/2017 to 1/14/2019 and contains 1,851,924 rows. Generally speaking, the bikeshare dataset contains fields for GPS coordinates, Trip ID, Events (i.e. Docking/Undocking/Pausing), User ID, Date and Time. Bikeshare data analysis could help us locate new bikeshare stations based on current usage patterns or figure out what months/days/times are most popular. Data visualization would help with these questions. The students could even go much further to overlay GIS terrain info and make a model that predicts how much rebalancing a new station at the top of a hill might need based on elevation. This could be based on existing trip data for the number of trips that “start at” versus the number “that end at” higher elevations. Or, students could combine our data with historic weather data to see how much weather conditions affect ridership. We’re open to any insights that the students can discover." - Provided by mBike for the challenge (http://datachallenge.ischool.umd.edu/datasets/)
