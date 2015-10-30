from math import sqrt, acos, degrees

# Retorna el angulo en grados formado por las aristas ab y ac.
def angulo_triangulo(a,b,c):
    ab = sqrt((a[0] - b[0])**2  + (a[1] - b[1])**2)
    bc = sqrt((b[0] - c[0])**2  + (b[1] - c[1])**2)
    ac = sqrt((a[0] - c[0])**2  + (a[1] - c[1])**2)
    ang = acos((ab**2 + ac**2 - bc**2)/(2*ab*ac))
    return degrees(ang)