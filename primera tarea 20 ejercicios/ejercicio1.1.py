class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, cantidad):
        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota {i + 1}: "))

            if self.validar_nota(nota):
                self.notas.append(nota)
            else:
                print("Nota inválida. Debe estar entre 0 y 100.")

        return self.notas

    def promedio(self):
        if not self.notas:
            return 0.0

        return sum(self.notas) / len(self.notas)


c = Calificador()

cantidad = int(input("¿Cuántas notas desea ingresar?: "))

print("Notas válidas:", c.cargar_notas(cantidad))
print("El promedio es:", c.promedio())