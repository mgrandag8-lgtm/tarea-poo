class RegistroNotas:
    def __init__(self):
        self.registros = {}

    def registrar(self, estudiante, nota):
        self.registros[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [
            estudiante for estudiante, nota in self.registros.items()
            if nota >= nota_minima
        ]

    def mejor_estudiante(self):
        if not self.registros:
            return None

        mejor = max(self.registros.items(), key=lambda item: item[1])
        return mejor


rn = RegistroNotas()

cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

for i in range(cantidad):
    print("\nEstudiante", i + 1)

    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota: "))

    rn.registrar(nombre, nota)


nota_minima = float(input("\nIngrese la nota mínima para aprobar: "))

print("Estudiantes aprobados:", rn.estudiantes_aprobados(nota_minima))
print("Mejor estudiante:", rn.mejor_estudiante())