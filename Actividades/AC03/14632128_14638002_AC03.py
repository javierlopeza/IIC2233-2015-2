class Rational():
    def __init__(self, numerador, denominador):
        self.numerador = (self.simplificar(numerador,denominador))[0]
        self.denominador = (self.simplificar(numerador,denominador))[1]
        if self.denominador<0:
            self.denominador *= -1
            self.numerador *= -1
    
    def __repr__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return str(self.numerador)+'/'+str(self.denominador)

    def simplificar(self, numerador, denominador):
        numerador = int(numerador)
        denominador = int(denominador)
        a = max(numerador, denominador)
        b = min(numerador, denominador)
        while b!=0:
            mcd = b
            b = a%b
            a = mcd
        numerador_sim = int(numerador/mcd)
        denominador_sim = int(denominador/mcd)
        if denominador_sim == 1:
            numerador_nuevo = numerador_sim
            denominador_nuevo = 1
        else:
            numerador_nuevo = numerador_sim
            denominador_nuevo = denominador_sim
        return [numerador_nuevo,denominador_nuevo]


    def __add__(self, otro_numero):
        num_nuevo = (self.numerador*otro_numero.denominador)+(self.denominador*otro_numero.numerador)
        den_nuevo = self.denominador*otro_numero.denominador
        resultado_suma = self.simplificar(num_nuevo,den_nuevo)
        num_suma = Rational(resultado_suma[0],resultado_suma[1])
        return num_suma

    def __sub__(self, otro_numero):
        num_nuevo = (self.numerador*otro_numero.denominador)-(self.denominador*otro_numero.numerador)
        den_nuevo = self.denominador*otro_numero.denominador
        resultado_resta = self.simplificar(num_nuevo,den_nuevo)
        num_resta = Rational(resultado_resta[0],resultado_resta[1])
        return num_resta

    def __mul__(self, otro_numero):
        num_nuevo = self.numerador*otro_numero.numerador
        den_nuevo = self.denominador*otro_numero.denominador
        resultado_mult = self.simplificar(num_nuevo, den_nuevo)
        num_mult = Rational(resultado_mult[0],resultado_mult[1])
        return num_mult

    def __truediv__(self, otro_numero):
        num_nuevo = self.numerador*otro_numero.denominador
        den_nuevo = self.denominador*otro_numero.numerador
        resultado_div = self.simplificar(num_nuevo, den_nuevo)
        num_div = Rational(resultado_div[0],resultado_div[1])
        return num_div

    def __lt__(self, otro_numero):
        m1 = self.numerador*otro_numero.denominador
        m2 = self.denominador*otro_numero.numerador
        return m1<m2

    def __gt__(self, otro_numero):
        m1 = self.numerador*otro_numero.denominador
        m2 = self.denominador*otro_numero.numerador
        return m1>m2

    def __le__(self,otro_numero):
        m1 = self.numerador*otro_numero.denominador
        m2 = self.denominador*otro_numero.numerador
        return m1<=m2

    def __ge__(self,otro_numero):
        m1 = self.numerador*otro_numero.denominador
        m2 = self.denominador*otro_numero.numerador
        return m1>=m2

    def __eq__(self,otro_numero):
        m1 = self.numerador*otro_numero.denominador
        m2 = self.denominador*otro_numero.numerador
        return m1==m2




if __name__ == "__main__":
    r1 = Rational(26, 4)
    r2 = Rational(-2, 6)
    r3 = Rational(34, 7)

    # 13/2 -1/3 34/7
    print(r1, r2, r3, sep=", ")

    # [Rational(1), Rational(-11/2)]
    print([Rational(1, 1), Rational(22, -4)])

    # 41/6
    print(r1 - r2)

    # 221/7
    print(r1 * r3)

    # 7/5
    print(r2 / Rational(5, -7))

    # True
    print(Rational(-4, 6) < Rational(1, -7))

    # True
    print(Rational(12, 8) == Rational(-24, -16))