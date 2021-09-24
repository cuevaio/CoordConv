from math import cos, sin, pi, tan

class Angle:
    def __init__(self, deg):
        self.deg = deg
        self.rad = deg*pi/180

        self.cos = cos(self.rad)
        self.sin = sin(self.rad)
        self.tan = tan(self.rad)

        self.cos2 = cos(self.rad)**2
        self.sin2 = sin(self.rad)**2

class Ellipsoid:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a**2/b
        
        self.e2 = (a**2 - b**2) / a**2
        self.ep2 = (a**2 - b**2) / b**2