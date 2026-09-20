class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, cantidad):
        self.pares = []
        self.impares = []

        for i in range(cantidad):
            num = int(input(f"Ingrese el número {i + 1}: "))

            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)

        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


an = AnalizadorNumeros()

cantidad = int(input("¿Cuántos números desea ingresar?: "))

print(an.separar(cantidad))
print("Cantidad de pares:", an.cantidad_pares_impares()[0])
print("Cantidad de impares:", an.cantidad_pares_impares()[1])