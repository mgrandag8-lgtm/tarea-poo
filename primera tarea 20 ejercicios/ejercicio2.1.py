class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, cantidad):
        for i in range(cantidad):
            palabra = input(f"Ingrese la palabra {i + 1}: ")
            self.agregar_palabra(palabra)


at = AnalizadorTexto()

cantidad = int(input("¿Cuántas palabras desea ingresar?: "))

at.agregar_multiples(cantidad)

print("Las palabras únicas son:", at.orden_palabras)
print("El número de palabras únicas es:", at.contar_palabras())