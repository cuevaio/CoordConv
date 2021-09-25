import csv
import re

from glob import glob
from exif import Image

from lib.functions import toDecimal

pathList = glob("photos/*.jpg")
with open('./input.csv', mode='w') as csv_file:
    fieldnames = ["ID", "Latitud", "Longitud", "Altitud"]
    
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for path in pathList:
        image_file = open(path, mode='rb')
        image = Image(image_file)

        lat = toDecimal(image.gps_latitude)
        long = toDecimal(image.gps_longitude)
        alt = round(image.gps_altitude,6)

        data = {
            "ID" : re.findall('[0-9]+', path)[0],
            "Latitud" : lat if image.gps_latitude_ref == "N" else -lat,
            "Longitud" : long if image.gps_longitude_ref == "E" else -long,
            "Altitud" : alt if image.gps_altitude_ref == 0  else -alt
        }

        csv_writer.writerow(data)

        image_file.close()


    

