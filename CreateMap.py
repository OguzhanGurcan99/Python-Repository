import folium
import pyproj

highlight1 = data['features'][56]["geometry"]["coordinates"]
highlight2 = data['features'][91]["geometry"]["coordinates"]

def mytransform(x, y):
  return pyproj.Transformer.from_crs("EPSG:3857", "EPSG:4326").transform(x, y)

transformed_highlight1 = mytransform(highlight1[0], highlight1[1])
transformed_highlight2 = mytransform(highlight2[0], highlight2[1])

map = folium.Map(location= transformed_highlight1, zoom_start=16)

folium.Marker(location = transformed_highlight1, popup='Point 1', icon=folium.Icon()).add_to(map)
folium.Marker(location = transformed_highlight2, popup='Point 2', icon=folium.Icon()).add_to(map)

title_html = '''<h3 align="center" style="font-size:20px"><b>Closest two points</b></h3>'''
map.get_root().html.add_child(folium.Element(title_html))

#raise NotImplementedError()
map.save("mymap.html")
