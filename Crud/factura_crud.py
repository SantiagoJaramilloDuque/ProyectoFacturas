from Modelo.factura import Factura

def crear_factura(cliente):
    factura = Factura(cliente)
    cliente.agregarFactura(factura)
    return factura

def agregar_producto_a_factura(factura, producto):
    factura.agregarProducto(producto)

def mostrar_factura(factura):
    factura.mostrarFactura()

def listar_facturas(cliente):
    return cliente.historialCompras
