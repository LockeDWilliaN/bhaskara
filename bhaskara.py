from math import sqrt
import time

class calculadora():
    def inicio(self):
        tentativas = 0
        max_tentativas = 3
        while tentativas < max_tentativas:
            try:
                self.a = int(input("Digite o Valor de A: "))
                self.b = int(input("Digite o valor de B: "))
                self.c = int(input("Digite o valor de C: "))
                return self.a, self.b, self.c
            except ValueError:
                tentativas += 1
                if tentativas == max_tentativas:
                    sair = input("Deseja sair do programa? [s/n] ")
                    if sair.lower() == "s":
                        print("Obrigado por utilizar o programa!")
                        time.sleep(3)
                        exit()
                    else:
                        tentativas = 0
                print("Por favor, digite um número\nTente Novamente")

    def calcular_bhaskara(self, a, b, c):
        delta = (b ** 2) - (4 * a * c)
        x, xv, yv = None, None, None
        if delta > 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            xv = -b / (2 * a)
            yv = -delta / (4 * a)
            return x1, x2, yv, xv, delta
        if delta == 0:
            x = -b / (2 * a)
            return x, x, xv, yv, delta
        print("ERRO! Delta não pode ser menor que ZERO")
        time.sleep(3)
        exit()  # NEED TO go back to first function and start over

    def results(self, delta, x1, x2, yv, xv):
        resultado = calculadora.calcular_bhaskara(self, self.a, self.b, self.c)
        x1, x2, xv, yv, delta = resultado
        print(f"\nValor de Delta: {delta:.2f}\n")
        print(f"Valor de X¹: {x1:.2f}")
        print(f"Valor de X²: {x2:.2f}\n")
        print(f"Valor de Xvértice: {xv:.2f}")
        print(f"Valor de Yvértice: {yv:.2f}")
        time.sleep(20)  #start over instead of exiting

if __name__ == "__main__": 
    calc = calculadora()  
    a, b, c = calc.inicio()
    delta, x1, x2, yv, xv = calc.calcular_bhaskara(a, b, c)
    calc.results(delta, x1, x2, yv, xv)  