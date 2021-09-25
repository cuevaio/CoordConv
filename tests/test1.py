import sys
sys.path.insert(1, '/home/tonycueva/UTEC/CoordConv')

import csv
from os import sep

from lib.functions import toCART, toUTM, toDecimal
from lib.classes import Ellipsoid

WGS84 = Ellipsoid(6378137, 6356752.21424)

# Test 1
PI01 = {}
PI01["lat"] = (5,10,47.79159)
PI01["lat"] = -toDecimal(PI01["lat"])

PI01["long"] = (80,37,39.96811)
PI01["long"] = -toDecimal(PI01["long"])

PI01["h"] = 52.1877

(PI01["Este (m)"],PI01["Norte(m)"],PI01["Huso"]) = toUTM(PI01["lat"],PI01["long"],WGS84)
(PI01["X (m)"],PI01["Y (m)"],PI01["Z (m)"]) = toCART(PI01["lat"],PI01["long"],PI01["h"],WGS84)

truePI01 = {
    'lat': -5.179942, 
    'long': -80.627769, 
    'h': 52.1877, 
    'Este (m)': 541252.2564, 
    'Norte (m)': 9427433.0234, 
    'Huso': 17, 
    'X (m)': 1034460.3737, 
    'Y (m)': -6267518.6437, 
    'Z (m)': -572008.7368
}

diff = {k: round(PI01.get(k, 0) - truePI01.get(k, 0), 6) for k in set(PI01)}

PI01["ID"] = "Calculado"
truePI01["ID"] = "IGN"
diff["ID"] = "Diferencia"

with open('./tests/test1.csv', mode='w') as csv_file:
    fieldnames = ["ID","Este (m)","Norte (m)","Huso", "X (m)","Y (m)", "Z (m)"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|",extrasaction='ignore')

    csv_writer.writeheader()
    csv_writer.writerow(truePI01)
    csv_writer.writerow(PI01)
    csv_writer.writerow(diff)
