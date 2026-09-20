class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [
            nombre for nombre, edad in self.personas.items()
            if edad >= edad_minima
        ]

    def edad_promedio(self):
        if not self.personas:
            return 0.0

        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()

cantidad = int(input("¿Cuántas personas desea ingresar?: "))

for i in range(cantidad):
    print("Persona", i + 1)

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    gp.agregar_persona(nombre, edad)


edad_minima = int(input("Ingrese la edad mínima que desea buscar: "))

print("Personas que cumplen con la edad mínima:",
      gp.personas_mayores(edad_minima))

print("Edad promedio:", gp.edad_promedio())