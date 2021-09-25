import csv

from lib.functions import toCART, toUTM
from lib.classes import Ellipsoid

WGS84 = Ellipsoid(6378137, 6356752.21424)

with open('input.csv') as input_file:
    csv_reader = csv.DictReader(input_file)

    with open('output.csv', mode='w') as output_file:
        fieldnames = ["ID","Latitud","Longitud","Elevación Elipsoidal (m)", "Este (m)","Norte (m)","Huso", "X (m)","Y (m)", "Z (m)"]
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for row in csv_reader:
            ID = row["ID"]

            lat = float(row["Latitud"])
            long = float(row["Longitud"])
            h = float(row["Altitud"])

            (E,N,huso) = toUTM(lat,long,WGS84)
            (X,Y,Z) = toCART(lat,long,h,WGS84)


            data = {
                "ID" : ID,
                "Latitud" : lat,
                "Longitud" : long,
                "Elevación Elipsoidal (m)" : h,
                "Este (m)" : E,
                "Norte (m)" : N,
                "Huso" : huso,
                "X (m)" : X,
                "Y (m)" : Y,
                "Z (m)" : Z
            }

            csv_writer.writerow(data)

