class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None

        return max(self.equipos, key=lambda eq: len(self.equipos[eq]))


eq = Equipos()

cantidad_equipos = int(input("¿Cuántos equipos desea crear?: "))

for i in range(cantidad_equipos):
    print("\nEquipo", i + 1)

    nombre_equipo = input("Ingrese el nombre del equipo: ")
    eq.crear_equipo(nombre_equipo)

    cantidad_jugadores = int(input("¿Cuántos jugadores tendrá este equipo?: "))

    for j in range(cantidad_jugadores):
        jugador = input(f"Ingrese el jugador {j + 1}: ")
        eq.agregar_jugador(nombre_equipo, jugador)


print("\nEquipos registrados:", eq.equipos)
print("El equipo con más integrantes es:", eq.equipo_mayor_integrantes())