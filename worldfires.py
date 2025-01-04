import csv
import plotly.express as px

filename= 'C:\\Users\\Kevin\\Desktop\\TEST.PY\\data\\world_fires_1_day.csv'
with open (filename)as f:
    reader= csv.reader(f)
    header_row= next(reader)

    lats,lons,brightness=[],[],[]
    
    for row in reader:
        lat= float(row[0])
        lon= float(row[1])
        bright= float(row[2])

        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)


fig= px.scatter_geo(lon=lons,lat=lats,title="world fires",color=brightness,color_continuous_scale="hot",range_color=brightness,labels={'color':"How Hot"},size=[7*bright for bright in brightness])
fig.show()