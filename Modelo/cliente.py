class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.historialCompras = []

    def agregarFactura(self, factura):
        self.historialCompras.append(factura)
