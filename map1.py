import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def elevColour(elevation):
    if elevation < 2000:
        return 'green'
    elif  2000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start = 6, tiles ="Mapbox Bright")


fg = folium.FeatureGroup(name = "Populations") #to keep code organized, another layer, a point layer for features

fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), #added polygons using geojson
style_function= lambda x: {'fillColor':'#fdf200' if x['properties']['POP2005'] < 5000000 #inline function
else '#ffdc07' if 5000000 <= x['properties']['POP2005'] < 10000000
else '#ffb607' if 10000000 <= x['properties']['POP2005'] < 15000000
else '#ff8407' if 15000000 <= x['properties']['POP2005'] < 20000000
else '#fd560e' if 20000000 <= x['properties']['POP2005'] < 25000000
else '#fd0e0e' if 25000000 <= x['properties']['POP2005'] < 30000000
else '#be05ff'}))

fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, el in zip(lat, lon, elev): #combines both lists
    fgv.add_child(folium.CircleMarker(location= [lt, ln], radius = 4, color = elevColour(el), fill = True, fill_opacity = 0.7, popup= str(el) + "m"))



map.add_child(fg)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Map1.html")
