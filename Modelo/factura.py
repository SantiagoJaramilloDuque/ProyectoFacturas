from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.fecha = datetime.now()
        self.productos = []
        self.valorTotal = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)
        self.valorTotal += producto.valor

    def mostrarFactura(self):
        print(f"\nFactura para {self.cliente.nombre}")
        print(f"Fecha: {self.fecha}")
        print("Productos:")
        for producto in self.productos:
            print(f"- {producto.nombre} ({producto.valor})")
        print(f"Valor Total: {self.valorTotal}")
