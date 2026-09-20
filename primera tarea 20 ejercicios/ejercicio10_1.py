class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [
            tarea for tarea in self.lista_tareas
            if tarea[1].lower() == "alta"
        ]

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [
            tarea for tarea in self.lista_tareas
            if tarea[0] != descripcion
        ]


t = Tareas()

cantidad = int(input("¿Cuántas tareas desea ingresar?: "))

for i in range(cantidad):
    print("\nTarea", i + 1)

    descripcion = input("Ingrese la descripción de la tarea: ")
    prioridad = input("Ingrese la prioridad (alta, media o baja): ")

    t.agregar_tarea(descripcion, prioridad)


print("\nTodas las tareas:", t.lista_tareas)
print("Tareas de prioridad alta:", t.tareas_prioritarias())

eliminar = input("\nIngrese la tarea completada que desea eliminar: ")

t.eliminar_completada(eliminar)

print("Tareas restantes:", t.lista_tareas)