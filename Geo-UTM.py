from math import cos, sin, pi, log
print("Hello world!")

def toRad(deg):
    return deg * pi / 180

class Angle:
    def __init__(self, deg):
        self.deg = deg
        self.rad = toRad(deg)

class Ellipsoid:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ep2 = (a**2 - b**2) / b**2
        self.c = a**2/b

def toUTM(lat, long, elip):
    lat = Angle(lat)
    long = Angle(long)

    v = elip.c * 0.9996 / (1 + elip.ep2 * (cos(lat.rad)**2))
    huso = round(long.deg/6 + 31)

    dLong = Angle(long.deg - huso * 6 + 183)
    
    A = cos(lat.rad)*sin(dLong.rad)

    xi = 0.5 * log((1 + A)/(1 - A))
    
    zeta = elip.ep2/2 * xi * (cos(lat.rad))**2

    X = xi * v * (1 + zeta/3) + 500000

    return(X)


myEllip = Ellipsoid(6378137.0, 6356752.3)

ans = toUTM(-12.135177, -77.022269, myEllip)

print(ans, myEllip.c, myEllip.ep2)

error = (ans - 279925.997014878)/279925.997014878
print(error)
