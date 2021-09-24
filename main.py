import csv

from lib.functions import toCART, toUTM
from lib.classes import Ellipsoid, Angle

# Assumptions:
WGS84 = Ellipsoid(6378137, 6356752.21424)
h = 52.1877

with open('input.csv') as input_file:
    csv_reader = csv.DictReader(input_file)

    with open('output.csv', mode='w') as output_file:
        fieldnames = ["Nombre","Latitud","Longitud","Elevación Elipsoidal (m)", "Este (m)","Norte (m)","Huso", "X (m)","Y (m)", "Z (m)"]
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for row in csv_reader:
            name = row["Nombre"]

            lat = Angle(float(row["Latitud"]))
            long = Angle(float(row["Longitud"]))
            # h = row["Elevación Elipsoidal (m)"]

            (E,N,huso) = toUTM(lat,long,WGS84)
            (X,Y,Z) = toCART(lat,long,h,WGS84)


            coord = {
                "Nombre" : name,
                "Latitud" : lat.deg,
                "Longitud" : long.deg,
                "Elevación Elipsoidal (m)" : h,
                "Este (m)" : E,
                "Norte (m)" : N,
                "Huso" : huso,
                "X (m)" : X,
                "Y (m)" : Y,
                "Z (m)" : Z
            }

            csv_writer.writerow(coord)