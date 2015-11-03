from math import sqrt


# Recibe los puntos a, b y entrega el vector unitario de a a b.
def vector_unitario(a, b):
    vx = b[0] - a[0]
    vy = b[1] - a[1]
    norma = sqrt(vx ** 2 + vy ** 2)
    try:
        vx /= norma
        vy /= norma
        vx = round(vx, 3)
        vy = round(vy, 3)
        return [vx, vy]
    except:
        return [0, 1]
