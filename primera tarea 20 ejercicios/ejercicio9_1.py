class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteos = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for char in texto:
            if char.isdigit():
                conteos["digitos"] += 1

            elif char.isalpha():
                if self.solo_vocales(char):
                    conteos["vocales"] += 1
                else:
                    conteos["consonantes"] += 1

        return conteos


astr = AnalizadorString()

texto = input("Ingrese un texto: ")

resultado = astr.contar_por_tipo(texto)

print("Cantidad de vocales:", resultado["vocales"])
print("Cantidad de consonantes:", resultado["consonantes"])
print("Cantidad de dígitos:", resultado["digitos"])
print("Texto más largo:", astr.texto_mas_largo)