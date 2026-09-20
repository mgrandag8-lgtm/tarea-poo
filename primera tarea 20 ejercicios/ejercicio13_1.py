class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []

        max_len = max(len(lista1), len(lista2))

        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado


cl = CombinadorListas()

lista1 = []
lista2 = []

cantidad1 = int(input("¿Cuántos elementos tendrá la lista 1?: "))

for i in range(cantidad1):
    numero = int(input(f"Ingrese el elemento {i + 1} de la lista 1: "))
    lista1.append(numero)


cantidad2 = int(input("¿Cuántos elementos tendrá la lista 2?: "))

for i in range(cantidad2):
    numero = int(input(f"Ingrese el elemento {i + 1} de la lista 2: "))
    lista2.append(numero)


print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Listas intercaladas:", cl.intercalar(lista1, lista2))