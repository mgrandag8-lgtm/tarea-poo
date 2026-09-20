class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        return [
            producto for producto, cantidad in self.stock.items()
            if cantidad < minimo
        ]


inv = Inventario()

cantidad_productos = int(input("¿Cuántos productos desea ingresar?: "))

for i in range(cantidad_productos):
    print("\nProducto", i + 1)

    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))

    inv.agregar_stock(producto, cantidad)


print("\nInventario actual:", inv.stock)

producto_restar = input("\nIngrese el producto al que desea restar stock: ")
cantidad_restar = int(input("Ingrese la cantidad que desea restar: "))

if inv.restar_stock(producto_restar, cantidad_restar):
    print("Stock restado correctamente.")
else:
    print("No hay suficiente stock o el producto no existe.")

minimo = int(input("\nIngrese el stock mínimo: "))

print("Inventario actualizado:", inv.stock)
print("Productos con bajo stock:", inv.productos_bajo_stock(minimo))