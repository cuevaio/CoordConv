from toCART import toCART
from classes import Angle, Ellipsoid
from toUTM import toUTM
from toCART import toCART


# Input:
WGS84 = Ellipsoid(6378137, 6356752.21424)
lat = Angle((5 + 10/60 + 47.79159/3600)*-1)
long = Angle((80 + 37/60 + 39.96811/3600)*-1)

lat = Angle(-12.135177)
long = Angle(-77.022269)
h = 52.1877

# 
(E,N,huso) = toUTM(lat,long, WGS84)
(X,Y,Z) = toCART(lat,long,h,WGS84)

print("Latitud   Longitud   Altura Elipsoidal")
print(round(lat.deg,6), round(long.deg,6), h)

print("\n\nEste          Norte          HUSO")
print(E,N,huso)

print("\n\nX              Y               Z")
print(X,Y,Z)
