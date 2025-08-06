import math


class Bhaskara:
    def delta(self, a, b, c,):
        return b ** 2 - 4 * a * c
    
    def main(self):
        a_digitado = float(input('Digite o valor de a: '))
        b_digitado = float(input('Digite o valor de b: '))
        c_digitado = float(input('Digite o valor de c: '))

        print(self.calcular_raizes(a_digitado, b_digitado, c_digitado))

    def calcular_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        
        if d < 0:
             return 0

        raiz_delta = math.sqrt(d)
        raiz1 = (-b  + raiz_delta) / (2 * a)

        if d == 0:
            return 1, raiz1

        raiz2 = (-b - raiz_delta) / (2 * a)

        return 2, raiz1, raiz2
    

if __name__ == '__main__':
    b = Bhaskara()
    b.main()
    b.main()