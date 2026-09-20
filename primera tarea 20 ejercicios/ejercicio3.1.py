class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]


c = CarroCompras()

cantidad = int(input("¿Cuántos artículos desea ingresar?: "))

for i in range(cantidad):
    print("Artículo", i + 1)

    nombre = input("Ingrese el nombre del artículo: ")
    precio = float(input("Ingrese el precio del artículo: "))

    c.agregar_articulo(nombre, precio)


print("El total del carrito es:", c.total_carrito())

precio_min = float(input("Ingrese el precio mínimo: "))
precio_max = float(input("Ingrese el precio máximo: "))

print(
    "Artículos dentro del rango:",
    c.articulos_por_rango(precio_min, precio_max)
)