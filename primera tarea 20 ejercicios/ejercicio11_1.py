class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        resultado = []

        for rango in rangos:
            for num in rango:
                if num not in resultado:
                    resultado.append(num)

        return resultado


sr = SelectorRango()

inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

rango = sr.crear_rango(inicio, fin)

print("El rango creado es:", rango)