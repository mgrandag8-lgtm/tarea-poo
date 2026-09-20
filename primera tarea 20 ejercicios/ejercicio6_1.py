class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, cantidad):
        for i in range(cantidad):
            temp = float(input(f"Ingrese la temperatura {i + 1}: "))
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        if not self.temperaturas:
            return 0.0

        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()

cantidad = int(input("¿Cuántas temperaturas desea ingresar?: "))

gt.registrar_multiples(cantidad)

print("Temperaturas registradas:", gt.temperaturas)
print("Temperatura mínima:", gt.minima())
print("Temperatura máxima:", gt.maxima())
print("Promedio:", gt.promedio())