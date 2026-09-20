class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida


inv = InversorSecuencia()

cantidad = int(input("¿Cuántos números desea ingresar?: "))

lista = []

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    lista.append(numero)

print("Lista original:", lista)
print("Lista invertida:", inv.invertir_lista(lista))