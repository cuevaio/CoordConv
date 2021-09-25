# Conversión de coordenadas geográficas a UTM y Cartesianas

## Cómo usar

### 1. Importa lo necesario:
```python
from lib.functions import toCART, toUTM
from lib.classes import Ellipsoid
```
### 2. Define el elipsoide a utilizar:
Debes definir el elipsoide con el que se harán los cálculos. Para esto 
crea uno indicando sus semiejes mayor (a) y menor (b).
```python
WGS84 = Ellipsoid(a=6378137, b=6356752.21424)
```
### 3. Convierte
Para convertir a coordenadas UTM:
```python
(Este, Norte, huso) = toUTM(lat=-11.880944, long=-76.995881, ellip=WGS84)
# Output:
# Este = 282594.8131
# Norte = 8685831.5178
# huso = 18
```

Para convertir a coordenadas cartesianas:
```python
(X, Y, Z) = toCART(lat=-11.880944, long=-76.995881, h=423.3429, ellip=WGS84)
# Output:
# X = 1404762.0495
# Y = -6082697.8451
# Z = -1304604.4213
```

## Pruebas

La diferencia que existe entre las coordenadas obtenidas con este programa
y la data oficial del IGN sobre las estaciones permanentes [PI01](https://drive.google.com/drive/folders/15WrcwlHwmBHlvKQHwPnIxC7DtpS4ukIL) y [LI03](https://drive.google.com/drive/folders/14mzdKSNHapWAkQLqZ72NdTIhNqefLjfJ) es mínima.

### PI01 en Piura
ID|Este (m)|Norte (m)|Huso|X (m)|Y (m)|Z (m)
--|--------|---------|----|-----|-----|-----
IGN|541252.2564|9427433.0234|17|1034460.3737|-6267518.6437|-572008.7368
Calculado|541252.2471|9427433.0559|17|1034460.3649|-6267518.6471|-572008.7073
Diferencia|-0.0093|0.0325|0|-0.0088|-0.0034|0.0295


### LI03 en Lima
ID|Este (m)|Norte (m)|Huso|X (m)|Y (m)|Z (m)
--|--------|---------|----|-----|-----|-----
IGN|308088.32324|8675748.8402|18|1429102.1648|-6075125.0134|-1314694.9459
Calculado|308088.2923|8675748.8383|18|1429102.1331|-6075125.0146|-1314694.9541
Diferencia|-0.03094|-0.0019|0|-0.0317|-0.0012|-0.0082


## Ejemplo

**getCoords.py**


Se usa la libería [exif](https://pypi.org/project/exif/) para obtener:
* latitud
* longitud
* altitud (con respecto al nivel del mar)

de las fotos ubicadas en la carpeta [photos](https://drive.google.com/drive/folders/1Z-neYzGiRGOMyCtqXZAyyWBY7C_NxxUg?usp=sharing).


Estos datos se escriben en el archivo input.csv


**convertCoords.py**


Para los cálculos se usa el elipsoide **WGS84**.
Se convierte las coordenadas de las fotos a UTM y Cartesianas.
Estos datos es escriben en el archivo output.csv
