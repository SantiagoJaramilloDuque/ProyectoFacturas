from Modelo.cliente import Cliente
from Modelo.factura import Factura
from Modelo.producto import Producto
from Modelo.control_plagas import ControlPlagas
from Modelo.control_fertilizantes import ControlFertilizantes
from Modelo.antibiotico import Antibiotico


cliente1 = Cliente("Ana García", "123456789")

plaguicida = ControlPlagas("Insecticida X", 50, "ICA-123", 15, 7)
fertilizante = ControlFertilizantes("Fertilizante Y", 75, "ICA-456", 30, "2024-04-20")
antibiotico = Antibiotico("Amoxicilina", 100, 500, "Bovinos")

factura1 = Factura(cliente1)
factura1.agregarProducto(plaguicida)
factura1.agregarProducto(fertilizante)
factura1.agregarProducto(antibiotico)

cliente1.agregarFactura(factura1)

print("breakpoint") 