class AnalizadorPatrones:
    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        agrupadas = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in agrupadas:
                agrupadas[longitud] = []

            agrupadas[longitud].append(palabra)

        return agrupadas


ap = AnalizadorPatrones()

texto = input("Ingrese un texto: ")

print("Palabras agrupadas por longitud:")
print(ap.agrupar_por_longitud(texto))