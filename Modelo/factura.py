from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__fecha = datetime.now()
        self.__productos = []
        self.__valorTotal = 0

    def agregarProducto(self, producto):
        self.__productos.append(producto)
        self.__valorTotal += producto.valor

    def mostrarFactura(self):
        print(f"\nFactura para {self.__cliente.nombre}")
        print(f"Fecha: {self.__fecha}")
        print("Productos:")
        for producto in self.__productos:
            print(f"- {producto.nombre} ({producto.valor})")
        print(f"Valor Total: {self.__valorTotal}")

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, productos):
        self.__productos = productos

    @property
    def valorTotal(self):
        return self.__valorTotal

    @valorTotal.setter
    def valorTotal(self, valorTotal):
        self.__valorTotal = valorTotal