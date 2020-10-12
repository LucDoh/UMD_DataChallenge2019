# mBike Bikeshare Analysis  
## [Best in Community Integration at UMD's 2019 Data Challenge](https://datachallenge.ischool.umd.edu/data-challenge-2019/)

I participated in University of Maryland's 1-week data challenge with a team of 3 other students (Linda, Grace & Ruthwick), where we won Best Community Integration. We also consulted with a Professor of Urban Planning, Dr. Iseki. This repository contains the Jupyter notebooks I used to clean and transform data, perform EDA to answer our research questions, and make geospatial visualizations.

Using a combination of temporal and spatial analyses, we made recommendations to Zagster on how to improve their bike-share service in College Park, Maryland.

By analyzing the bike usage by station and making use of the 1/4 mile standard (an urban planning standard for how far people are willing to walk to a transit station), we predicted the three best new locations for stations. We also showed how the issue of bike imbalance emerges due to users' tendencies (people don't like going uphill), and gave estimates for how often stations would need to be rebalanced. Linda & Grace showed how usage varies seaonally, by day/time as well as with the weather (rain and temperature from NOAA).

The tools I used most were:
  * Jupyter Notebooks (Python)
  * Pandas
  * Seaborn
  * Folium

Our team also used Tableau and SAS.
  
***

### Dataset -  City of College Park mBike Bikeshare
"From 6/14/2017 to 1/14/2019 and contains 1,851,924 rows ... contains fields for GPS coordinates, Trip ID, Events (i.e. Docking/Undocking/Pausing), User ID, Date and Time. Bikeshare data analysis could help us locate new bikeshare stations based on current usage patterns or figure out what months/days/times are most popular. Data visualization would help with these questions. ... Or, students could combine our data with historic weather data to see how much weather conditions affect ridership. We’re open to any insights that the students can discover." - Provided by mBike (http://datachallenge.ischool.umd.edu/datasets/)
