import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename= "C:\\Users\\Kevin\\Desktop\\TEST.PY\\eq_data_1_day_m1.geojson"

with open(filename,encoding='utf8')as f:
    all_eq_data=json.load(f)

all_eq_dicts= all_eq_data['features']
titlle= all_eq_data['metadata']['title']

mags,lons,lats=[],[],[]

for eq in all_eq_dicts:
    mag = eq['properties']['mag']
    lon= eq['geometry']['coordinates'][0]
    lat= eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data=  [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[7*mag for mag in mags]
    }
}]
my_layout= Layout(title=titlle)

fig={'data':data,'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')

