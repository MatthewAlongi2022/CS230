import pandas as pd
import streamlit as st
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np

df_pubs = pd.read_csv("open_pubs_8000_sample.csv")

df_pubs.rename(columns={ "latitude": "Latitude","longitude":"Longitude"}, inplace= True)

st.title("England Pubs Map")
st.write(df_pubs)
local_authority= list(df_pubs["local_authority"])
st.write(local_authority)
local_authorities = []
for local in local_authority:
    if local.lower() not in local_authorities:
        local_authorities.append(local.lower())

st.write(local_authorities)
selected_local_authority = st.selectbox("Please Select a Category", local_authorities )

sub_df_list = []
s_df_u = df_pubs[df_pubs["local_authority"].str.lower() == "cornwall"]
st.write(s_df_u)

for c in local_authorities:
    sub_df = df_pubs[df_pubs["local_authority"].str.lower() == c]
    sub_df_list.append(sub_df)
sub_layers = []
for s_df in sub_df_list:
    sub_layer = pdk.Layer(type = 'ScatterplotLayer', # layer type
                      data=s_df, # data source
                      get_position='[Latitude, Longitude]', # coordinates
                      get_radius=500, # scatter radius
                      get_color=[0,0,255],   # scatter color
                      pickable=True # work with tooltip
                      )

    tool_tip = {"html": "Local Authority:<br/> <b>{Name}</b>",
                "style": { "backgroundColor": "orange",
                            "color": "white"}
                }
view_state = pdk.ViewState(
        latitude=df_pubs["Latitude"].mean(), # The latitude of the view center
        longitude=df_pubs["Longitude"].mean(), # The longitude of the view center
        zoom=11, # View zoom level
        pitch=0) # Tilt level

map = pdk.Deck(
        map_style='mapbox://styles/mapbox/outdoors-v11', # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
        initial_view_state=view_state,
        #layers=[layer1,layer2], # The following layer would be on top of the previous layers
        tooltip= tool_tip )


view_state = pdk.ViewState(
                latitude=df_pubs["Latitude"].mean(),
                longitude=df_pubs["Longitude"].mean(),
                zoom=11,
                pitch=0)



