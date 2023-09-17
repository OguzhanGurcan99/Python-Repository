import psycopg2
import folium
from geopy.geocoders import Nominatim

location = Nominatim(user_agent= "GetLoc")

conn = psycopg2.connect(database="postgres", user='postgres', password='1234', host='localhost', port='5432')

def Create_Map():
    file_name = input("Please enter an output file name : ")
    extension = ".html"
    print()

    cur = conn.cursor()
    cur.execute('''SELECT place  FROM events''')
    events_places = cur.fetchall()
    print("EVENT_PLACES ", [i[0].rstrip() for i in events_places])
    print()

    cur.execute('''SELECT  name,community_id,time  FROM events''')
    popup_information = cur.fetchall()
    print("POPUP INFORMATIONS ", [(i[0].rstrip(), i[1], i[2].rstrip()) for i in popup_information])
    print()

    index = 0
    Points = []
    map = folium.Map(location= None, zoom_start=16)

    for i in events_places:

        my_location = location.geocode(i)

        latitude = my_location.latitude
        longitude = my_location.longitude
        point = (latitude,longitude)

        Points.append(point)

        popup = popup_information[index][1] +" " + popup_information[index][0] + popup_information[index][2]
        index += 1

        folium.Marker(location = point, popup= popup, icon=folium.Icon()).add_to(map)

    title_html = '''<h3 align="center" style="font-size:20px"><b>CAMPUS SOCIAL ACTIVITIES MAP</b></h3>'''
    map.get_root().html.add_child(folium.Element(title_html))

    map.save(file_name+extension)
    message = "Users can find current campus activities in " + file_name + extension

    return map,Points,message


output = Create_Map()
for k in range(3):
    print(output[k])
    print()
