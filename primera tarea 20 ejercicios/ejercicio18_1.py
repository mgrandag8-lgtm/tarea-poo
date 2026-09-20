import math

class CalculadorDistancia:
    def distancia(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


cd = CalculadorDistancia()

x1 = float(input("Ingrese X1: "))
y1 = float(input("Ingrese Y1: "))
x2 = float(input("Ingrese X2: "))
y2 = float(input("Ingrese Y2: "))

resultado = cd.distancia(x1, y1, x2, y2)

print("La distancia es:", resultado)