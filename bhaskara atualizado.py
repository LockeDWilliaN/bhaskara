from math import sqrt

class Calculadora:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def calcular_bhaskara(self):
        delta = (self.b ** 2) - 4 * self.a * self.c
        xv = -self.b / (2 * self.a)
        yv = -delta / (4 * self.a)

        if delta > 0:
            if self.b >= 0: 
                x1 = (self.b + sqrt(delta)) / (2 * self.a)
                x2 = (self.b - sqrt(delta)) / (2 * self.a)
            else:
                x1 = (-self.b + sqrt(delta)) / (2 * self.a)
                x2 = (-self.b - sqrt(delta)) / (2 * self.a)
            return delta, x1, x2, xv, yv

        if delta == 0:
            x = -self.b / (2 * self.a)
            return delta, x, x, xv, yv
        
        if delta < 0:
            return None
    
    def results(self):
        resultado = self.calcular_bhaskara()

        if resultado is not None:
            delta, x1, x2, xv, yv = resultado
            print("\n--------------------------------")
            print(f"Valor de Delta: {delta:.1f}")
        
            if delta == 0:
                print("--------------------------------")
                print(f"Valor de X: {x1:.1f}")
                print("--------------------------------")
        
            if delta > 0:
                print("--------------------------------")
                print(f"Valor de X¹: {x1:.1f}")
                print(f"Valor de X²: {x2:.1f}")
                print("--------------------------------")
                

            if xv is not None and yv is not None:
                print(f"Valor de Xvértice: {xv:.1f}")
                print(f"Valor de Yvértice: {yv:.1f}")
                print("--------------------------------")

        else:
            print("\n--------------------------------")
            print("ERRO: delta < 0")
            print("--------------------------------")
            

a = int(input("Digite o Valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
    
if __name__ == '__main__':
    try:
        calc = Calculadora(a, b, c,)    
        calc.results()
    except ValueError as e:
        print(e)
    