from lib.functions import toCART, toUTM
from lib.classes import Ellipsoid

WGS84 = Ellipsoid(a=6378137, b=6356752.21424)

(Este, Norte, huso) = toUTM(lat=-11.880944, long=-76.995881, ellip=WGS84)
print(Este, Norte, huso)
# Output:
# Este = 282594.8131
# Norte = 8685831.5178
# huso = 18

(X, Y, Z) = toCART(lat=-11.880944, long=-76.995881, h=423.3429, ellip=WGS84)
print(X, Y, Z)
# Output:
# X = 1404762.0495
# Y = -6082697.8451
# Z = -1304604.4213