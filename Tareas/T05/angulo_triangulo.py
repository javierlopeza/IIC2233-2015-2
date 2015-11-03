from math import sqrt, acos, degrees


# Retorna el angulo en grados formado por el militar, la vertical y el mouse.
def angulo_triangulo_mouse(origen, guia, mouse):
    ab = sqrt((origen[0] - guia[0]) ** 2 + (origen[1] - guia[1]) ** 2)
    bc = sqrt((guia[0] - mouse[0]) ** 2 + (guia[1] - mouse[1]) ** 2)
    ac = sqrt((origen[0] - mouse[0]) ** 2 + (origen[1] - mouse[1]) ** 2)
    try:
        ang = acos((ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab * ac))
        ang = degrees(ang)
        if mouse[0] < 0 and mouse[1] < 0:
            ang *= -1
        if mouse[0] > 0 and mouse[1] < 0:
            ang *= -1
        if mouse[0] and mouse[1]:
            signo = (mouse[0] * mouse[1]) / abs(mouse[0] * mouse[1])
            ang *= signo
        return ang
    except:
        return 0


# Retorna el angulo en grados formado por el zombie, la vertical y el militar.
def angulo_triangulo_zombie(zombie, guia, militar):
    ab = sqrt((zombie[0] - guia[0]) ** 2 + (zombie[1] - guia[1]) ** 2)
    bc = sqrt((guia[0] - militar[0]) ** 2 + (guia[1] - militar[1]) ** 2)
    ac = sqrt((zombie[0] - militar[0]) ** 2 + (zombie[1] - militar[1]) ** 2)
    try:
        ang = acos((ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab * ac))
        ang = degrees(ang)
        if militar[0] < 0 and militar[1] < 0:
            ang *= -1
        if militar[0] > 0 and militar[1] < 0:
            ang *= -1
        if militar[0] and militar[1]:
            signo = (militar[0] * militar[1]) / abs(militar[0] * militar[1])
            ang *= signo
        return ang
    except:
        return 0
