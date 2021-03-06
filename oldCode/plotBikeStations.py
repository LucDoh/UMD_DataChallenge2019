#!/usr/bin/env python
# coding: utf-8

# In[3]:


import folium
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

df = pd.read_csv('trip_path_mbike_start_20190114.csv')
print("DF size is " + str(len(df.index)))
df.head(5)


# In[4]:


#Counts, not including background/foreground
plt.rcParams['figure.figsize'] = [10, 5]
dfx = df[(df['Bike_Event'] != 'Background') & (df['Bike_Event'] != 'Foreground')]
dfx = dfx[(dfx['Bike_Event'] != 'EndTripGeofenceDisabled') & (dfx['Bike_Event'] != 'AccessCodeBLEFallback')]
dfx = dfx[(dfx['Bike_Event'] != 'SentrilockAccessCodeShown') & (dfx['Bike_Event'] != 'OnHold')]
sns.countplot(dfx.Bike_Event)
dfx.Bike_Event.value_counts()


# In[5]:


df = df[(df['Bike_Event'] == 'StartTrip') | (df['Bike_Event'] == 'EndTripInsideGeofence')]
print("Only %s are Start/End trip events." % str(len(df.index)))

dfStart = df[df['Bike_Event'] == 'StartTrip']
dfEnd = df[df['Bike_Event'] == 'EndTripInsideGeofence']


# In[6]:


sns.countplot(df.Bike_Event)


# In[8]:

'''
# Marker Cluster
map_CP = folium.Map(location=[df.Coords_Latitude.mean(), df.Coords_Longitude.mean()], zoom_start=15)
mc = folium.plugins.MarkerCluster()
for i in range (0,len(df.index)):
    lat = df.Coords_Latitude.iloc[i]
    long = df.Coords_Longitude.iloc[i]
    mc.add_child(folium.Marker([lat,long]))#.add_to(map_CP)

map_CP.add_child(mc)


# In[100]:


# Marker Cluster
map_Start = folium.Map(location=[dfStart.Coords_Latitude.mean(), dfStart.Coords_Longitude.mean()], zoom_start=14.8)
mc1 = folium.plugins.MarkerCluster()

for i in range (0,1000):
    lat = dfStart.iloc[i].Coords_Latitude
    long = dfStart.iloc[i].Coords_Longitude
    mc1.add_child(folium.Marker([lat,long]))#.add_to(map_CP)

map_Start.add_child(mc1)


# In[95]:


map_End = folium.Map(location=[dfEnd.Coords_Latitude.mean(), dfEnd.Coords_Longitude.mean()], zoom_start=15)
mc2 = folium.plugins.MarkerCluster()

for i in range (0,1000):
    lat = dfEnd.iloc[i].Coords_Latitude
    long = dfEnd.iloc[i].Coords_Longitude
    mc2.add_child(folium.Marker([lat,long]))

map_End.add_child(mc2)
'''
