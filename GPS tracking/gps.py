import csv
from gmplot import gmplot


gmap = gmplot.GoogleMapPlotter(28.6812569, 77.32448912, 17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('worldcities.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    k = 0

    for row in reader:
        lat = float(row[2])
        long = float(row[3])

        if k == 0:
            gmap.marker(lat, long, 'yellow')
            k = 1
        else:
            gmap.marker(lat, long, 'blue')

gmap.marker(lat, long, 'red')
gmap.draw('my_map.html')