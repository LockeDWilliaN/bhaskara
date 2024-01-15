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
            print(f"Valor de Delta: {delta:.2f}")
        
            if delta == 0:
                print("--------------------------------")
                print(f"Valor de X: {x1:.2f}")
                print("--------------------------------")
        
            if delta > 0:
                print("--------------------------------")
                print(f"Valor de X¹: {x1:.2f}")
                print(f"Valor de X²: {x2:.2f}")
                print("--------------------------------")
                
            if xv is not None and yv is not None:
                print(f"Valor de Xvértice: {xv:.2f}")
                print(f"Valor de Yvértice: {yv:.2f}")
                print("--------------------------------\n")

        else:
            delta = resultado
            print("\n--------------------------------")
            print("A equação não possui raizes reais! (Delta < 0)")
            print("--------------------------------\n")
            
    
if __name__ == '__main__':
    tentativas = 0
    max_tentativas = 3
    while tentativas < max_tentativas:
        try:
            a = int(input("Digite o Valor de A: "))
            b = int(input("Digite o valor de B: "))
            c = int(input("Digite o valor de C: ")) 
            calc = Calculadora(a, b, c,)    
            calc.results()
            exit()
        except ValueError:
            tentativas += 1
            if tentativas == max_tentativas:
                sair = input("Deseja sair do programa? [s/n] ")
                if sair.lower() == "s":
                    print("Obrigado por utilizar o programa!")
                    exit()
                else:
                    tentativas = 0
            print("Por favor, digite um número\nTente Novamente")
            