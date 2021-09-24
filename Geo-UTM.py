from math import trunc, cos, sin, pi, log, atan, tan
print("Hello world!")

def toRad(deg):
    return deg * pi / 180

class Angle:
    def __init__(self, deg):
        self.deg = deg
        self.rad = toRad(deg)
        self.cos2 = cos(self.rad)**2
        self.cos = cos(self.rad)
        self.sin = sin(self.rad)
        self.tan = tan(self.rad)

class Ellipsoid:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ep2 = (a**2 - b**2) / b**2
        self.c = a**2/b

def toUTM(lat, long, ellip):
    v = ellip.c * 0.9996 / (1 + ellip.ep2 * lat.cos2)**0.5
    huso = trunc(long.deg/6 + 31)

    Δlong= Angle(long.deg - huso * 6 + 183)
    
    A = lat.cos*Δlong.sin

    ξ = 0.5 * log((1 + A)/(1 - A))
    
    ζ = ellip.ep2/2 * ξ * lat.cos2

    X = ξ * v * (1 + ζ/3) + 500000
    
    η = atan(lat.tan/Δlong.cos) - lat.rad
    
    α = 0.75 * ellip.ep2

    β = 5/3 * α**2

    γ = 35/27 * α**3

    A1 = sin(2*lat.rad)
    A2 = A1 * lat.cos2

    J2 = lat.rad + 0.5*A1
    J4 = 0.25 * (3*J2 + A2)
    J6 = (5*J4 + A2*lat.cos2)/3

    B = 0.9996 * ellip.c * (lat.rad - J2*α + J4*β - J6*γ)

    Y = η * v * (1+ζ) + B + 10**7


    return(round(X,6),round(Y,6), huso)


WGS84 = Ellipsoid(6378137, 6356752.21424)

lat = Angle((5 + 10/60 + 47.79159/3600)*-1)
long = Angle((80 + 37/60 + 39.96811/3600)*-1)

(X,Y,huso) = toUTM(lat,long, WGS84)
print("X             Y              HUSO")
print(X,Y,huso)

