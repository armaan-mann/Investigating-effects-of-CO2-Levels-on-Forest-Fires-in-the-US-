"""
Part 2: Visual Representation of the Forest Fires in US (Map) (2010 - 2015)
Objective: In this part the forst fires data of 10 years
has been shrink down to just 5 years which from 2010 to 2015 of the US.
The map opens up in the browser with some features:
    - Ability to Zoom in and out
    - Ability to move around the map.
    - Each marker on the US map provides basic insights of the forest fires.
"""
# Importing Packages
import os
import webbrowser
import folium
import pandas as pd
from folium import plugins
from main import read_file_map


############################################################################################
# The function below generates the map of the whole world.
# Only the US within the map has borders.
# Markers are placed depending on the corresponding latitude and longitudes.
# Each marker contains some information of the forest fire.
############################################################################################
def make_map() -> None:
    """
    Generate a map of US with forest fires from years 2010 to 2015.
    """
    # Extracting the data using the function above
    fire_data = read_file_map('FireData5yrs.csv')

    # Creating a data frame
    container = pd.DataFrame({
        'lon': fire_data['Longitude'],
        'lat': fire_data['Latitude'],
        'Size': fire_data['Fire Size'],
        'Veg': fire_data["Vegetation"],
        'FMag': fire_data["Fire Magnitude"],
        'Wind': fire_data['Wind Contained'],
        'Humid': fire_data['Humid Contained'],
        'remote': fire_data['Remoteness'],
        'link': fire_data['Links'],
        'time': fire_data['Time']
    })

    # Creates the Map
    m = folium.Map(location=[39.525501, -102.163384], zoom_start=3, prefer_canvas=True, tiles='Stamen Terrain')

    # Overlay of the US
    outline_us = os.path.join('overlay.json')

    # Creating a Marker Cluster
    cluster = folium.plugins.MarkerCluster(name="Markers").add_to(m)

    x = pd.read_csv('FireData5yrs.csv')

    # Adding a heat map:
    folium.Choropleth(
        geo_data=outline_us,
        data=x,
        columns=['state', 'fire_mag'],
        name='Fire Magnitude',
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name='idk',
        highlight=True).add_to(m)

    # Iterating through the data and at each iteration adding its value.
    # It creates the marker and the popup with these information inside the popup.
    for i in range(0, len(container)):
        info_size = '<strong> Fire Size </strong>:' + container.iloc[i]['Size'] + 'g/mi'
        info_veg = '<strong> Vegetation </strong>:' + container.iloc[i]['Veg']
        info_mag = '<strong> Fire Magnitude </strong>:' + container.iloc[i]['FMag']
        info_wind = '<strong> Wind Contained </strong>:' + container.iloc[i]['Wind']
        info_humid = '<strong> Humidity Contained </strong>:' + container.iloc[i]['Humid']
        info_remote = '<strong> Remoteness </strong>:' + container.iloc[i]['remote']
        info_link = container.iloc[i]['link']
        info_time = '<strong> Year </strong>:' + container.iloc[i]['time']
        info_all = info_mag + '<br>' + info_time + '<br>' + info_veg + '<br>' + info_wind + '<br>' + \
                   info_humid + '<br>' + info_remote + '<br>' + info_size + '<br>' + \
                   '<a href=' + info_link + ' > [More Details] </ a >'
        (folium.Marker([container.iloc[i]['lat'], container.iloc[i]['lon']],
                       popup=folium.Popup(info_all, max_width=280, min_width=280),
                       icon=folium.Icon(color='red', icon='fa-fire', prefix='fa'),
                       tooltip='Click For More Information').add_to(cluster))

    # Add the outline to map
    folium.GeoJson(outline_us, name='America').add_to(m)

    # Adding a Mini Map
    mini = plugins.MiniMap(toggle_display=True)
    m.add_child(mini)

    # plugins.ScrollZoomToggler().add_to(m)
    plugins.Fullscreen(position='topright').add_to(m)

    # Adding More types of maps
    folium.TileLayer('OpenStreetMap').add_to(m)
    folium.TileLayer('Stamen Watercolor').add_to(m)
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('CartoDB positron').add_to(m)
    folium.TileLayer('CartoDB dark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    # Saves the Map
    m.save('m.html')

    # Opens the Webpage
    webbrowser.open('m.html')


# if __name__ == '__main__':
#     import python_ta
#
#     python_ta.check_all(config={
#         'allowed-io': ['graph_data', 'main', 'read_file_2'],
#         'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
#                           'plotly.graph_objects', 'plotly.subplots', 'numpy',
#                           'matplotlib.pyplot', 'folium', 'pandas', 'os', 'webbrowser', 'main',
#                           'read_file_2'],
#         'max-line-length': 150,
#         'max-args': 6,
#         'max-locals': 25,
#         'disable': ['R1705', 'E9989'],
#     })
#
#     import python_ta.contracts
#
#     python_ta.contracts.DEBUG_CONTRACTS = False
#     python_ta.contracts.check_all_contracts()
