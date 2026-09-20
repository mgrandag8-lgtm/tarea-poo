class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, cantidad):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for i in range(cantidad):
            edad = int(input(f"Ingrese la edad {i + 1}: "))

            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades_cat = self.grupos.get(categoria, [])

        if not edades_cat:
            return 0.0

        return sum(edades_cat) / len(edades_cat)


ae = AgrupadorEdades()

cantidad = int(input("¿Cuántas edades desea ingresar?: "))

print("Grupos:", ae.agrupar_por_categoria(cantidad))

categoria = input(
    "Ingrese la categoría para calcular el promedio "
    "(niño, adolescente, adulto o mayor): "
)

print(
    "Edad promedio de la categoría:",
    ae.edad_promedio_categoria(categoria)
)