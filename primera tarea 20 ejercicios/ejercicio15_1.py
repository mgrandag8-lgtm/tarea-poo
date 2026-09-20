class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = [
            i for i in range(1, numero + 1)
            if numero % i == 0
        ]
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma_propios = sum(
            d for d in divisores
            if d != numero
        )

        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        return {
            num: self.encontrar_divisores(num)
            for num in numeros
        }


df = DivisorFinder()

numero = int(input("Ingrese un número: "))

print("Los divisores son:", df.encontrar_divisores(numero))

if df.es_perfecto(numero):
    print("El número es perfecto.")
else:
    print("El número no es perfecto.")