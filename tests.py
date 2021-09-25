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

# Test 2
LI03 = {}
LI03["lat"] = (11,58,25.09878)
LI03["lat"] = -toDecimal(LI03["lat"])

LI03["long"] = (76,45,45.03497)
LI03["long"] = -toDecimal(LI03["long"])

LI03["h"] = 698.8767

(LI03["Este (m)"],LI03["Norte(m)"],LI03["Huso"]) = toUTM(LI03["lat"],LI03["long"],WGS84)
(LI03["X (m)"],LI03["Y (m)"],LI03["Z (m)"]) = toCART(LI03["lat"],LI03["long"],LI03["h"],WGS84)

trueLI03 = {
    'lat': -11.973639, 
    'long': -11.973639, 
    'h': 698.8767, 
    'Este (m)': 308088.32324, 
    'Norte (m)': 8675748.8402, 
    'Huso': 18, 
    'X (m)': 1429102.1648, 
    'Y (m)': -6075125.0134, 
    'Z (m)': -1314694.9459
}

diff = {k: round(LI03.get(k, 0) - trueLI03.get(k, 0), 6) for k in set(LI03)}

LI03["ID"] = "Calculado"
trueLI03["ID"] = "IGN"
diff["ID"] = "Diferencia"

print(LI03)
with open('./tests/test2.csv', mode='w') as csv_file:
    fieldnames = ["ID","Este (m)","Norte (m)","Huso", "X (m)","Y (m)", "Z (m)"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|",extrasaction='ignore')

    csv_writer.writeheader()
    csv_writer.writerow(trueLI03)
    csv_writer.writerow(LI03)
    csv_writer.writerow(diff)