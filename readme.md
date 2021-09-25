# Conversión de coordenadas georáficas a UTM y Cartesianas

Se usa la libería [exif](https://pypi.org/project/exif/) para obtener:
* latitud
* longitud
* altitud (con respecto al nivel del mar)

de las fotos ubicadas en la carpeta [photos](https://drive.google.com/drive/folders/1Z-neYzGiRGOMyCtqXZAyyWBY7C_NxxUg?usp=sharing).

Para los cálculos se usa el elipsoide **WGS84**

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
Calculado|308088.2923||18|1429102.1331|-6075125.0146|-1314694.9541
Diferencia|-0.03094||0|-0.0317|-0.0012|-0.0082