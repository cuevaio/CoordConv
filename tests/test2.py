import sys
sys.path.insert(1, '/home/tonycueva/UTEC/CoordConv')

import csv
from os import sep

from lib.functions import toCART, toUTM, toDecimal
from lib.classes import Ellipsoid

WGS84 = Ellipsoid(6378137, 6356752.21424)

# Test 2
LI03 = {}
LI03["lat"] = (11,58,25.09878)
LI03["lat"] = -toDecimal(LI03["lat"])

LI03["long"] = (76,45,45.03497)
LI03["long"] = -toDecimal(LI03["long"])

LI03["h"] = 698.8767

(LI03["Este (m)"],LI03["Norte (m)"],LI03["Huso"]) = toUTM(LI03["lat"],LI03["long"],WGS84)
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

with open('./tests/test2.csv', mode='w') as csv_file:
    fieldnames = ["ID","Este (m)","Norte (m)","Huso", "X (m)","Y (m)", "Z (m)"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|",extrasaction='ignore')

    csv_writer.writeheader()
    csv_writer.writerow(trueLI03)
    csv_writer.writerow(LI03)
    csv_writer.writerow(diff)