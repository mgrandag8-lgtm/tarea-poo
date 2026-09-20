class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos_unicos = set()

        for inicio, fin in rangos:
            elementos_unicos.update(range(inicio, fin + 1))

        return sorted(list(elementos_unicos))


sr = SelectorRango()

cantidad = int(input("¿Cuántos rangos desea ingresar?: "))

rangos = []

for i in range(cantidad):
    print("\nRango", i + 1)

    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))

    rangos.append((inicio, fin))


resultado = sr.elementos_en_multiples_rangos(*rangos)

print("Elementos únicos de todos los rangos:", resultado)