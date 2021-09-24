def toCART(lat, long, h, ellip):
    N = ellip.a / (1 - ellip.e2 * lat.sin2)*0.5

    X = (N + h) * lat.cos * long.cos
    Y = (N + h) * lat.cos * long.sin    
    Z = (N * (1 - ellip.e2) + h) * lat.sin
    
    return (round(X,6),round(Y,6),round(Z,6))
