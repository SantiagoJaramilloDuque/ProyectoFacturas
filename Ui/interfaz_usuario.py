from Modelo.control_fertilizantes import ControlFertilizantes
from Modelo.control_plagas import ControlPlagas
from Modelo.antibiotico import Antibiotico
from Modelo.cliente import Cliente
from Modelo.factura import Factura

class InterfazUsuario:
    def __init__(self):
        self.clientes = {}
        self.productosDisponibles = [
            ControlFertilizantes("Fertilizante X", 50, "ICA-12345", 30, "2025-03-01"),
            ControlPlagas("Plaga Y", 30, "ICA-67890", 15, 10),
            Antibiotico("Antibiótico Z", 70, 500, "Bovinos")
        ]

    def mostrarProductos(self):
        print("\nProductos disponibles:")
        for i, producto in enumerate(self.productosDisponibles, 1):
            print(f"{i}. {producto.nombre} - ${producto.valor}")

    def agregarProductoaFactura(self, factura):
        self.mostrarProductos()
        try:
            seleccion = int(input("\nSeleccione el número del producto a agregar: "))
            if 1 <= seleccion <= len(self.productosDisponibles):
                factura.agregarProducto(self.productosDisponibles[seleccion - 1])
                print(f"\nProducto '{self.productosDisponibles[seleccion - 1].nombre}' agregado a la factura.")
            else:
                print("\nSelección inválida.")
        except ValueError:
            print("\nPor favor ingrese un número válido.")

    def crearFactura(self, cliente):
        factura = Factura(cliente)
        while True:
            self.agregarProductoaFactura(factura)
            continuar = input("¿Desea agregar otro producto? (s/n): ")
            if continuar.lower() != 's':
                break
        factura.mostrarFactura()
        cliente.agregarFactura(factura)
        print("\nFactura creada y añadida al historial del cliente.\n")
        input("Presione Enter para continuar...")

    def crearCliente(self):
        nombre = input("\nIngrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        cliente = Cliente(nombre, cedula)
        self.clientes[cedula] = cliente
        print(f"\nCliente '{nombre}' creado exitosamente.\n")
        input("Presione Enter para continuar...")
        return cliente

    def verHistorialCompras(self, cliente):
        print(f"\nHistorial de compras de {cliente.nombre}:")
        for factura in cliente.historialCompras:
            factura.mostrarFactura()

    def buscar_por_cedula(self, mensaje="Ingrese la cédula del cliente: "):
        cedulaCliente = input(f"\n{mensaje}")
        cliente = self.clientes.get(cedulaCliente)
        if not cliente:
            print("\nCliente no encontrado.")
            input("Presione Enter para continuar...")
        return cliente

    def mostrarMenu(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Crear Cliente")
            print("2. Crear Factura")
            print("3. Ver Historial de Compras de Cliente")
            print("4. Eliminar Cliente")
            print("5. Ver Productos Disponibles")
            print("6. Ver lista de clientes")
            print("7. Salir")
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.crearCliente()
                elif opcion == 2:
                    cliente = self.buscar_por_cedula()
                    if cliente:
                        self.crearFactura(cliente)
                elif opcion == 3:
                    cliente = self.buscar_por_cedula()
                    if cliente:
                        self.verHistorialCompras(cliente)
                        input("\nPresione Enter para continuar...")
                elif opcion == 4:
                    cliente = self.buscar_por_cedula("Ingrese la cédula del cliente a eliminar: ")
                    if cliente:
                        del self.clientes[cliente.cedula]
                        print("Cliente eliminado exitosamente.")
                        input("\nPresione Enter para continuar...")
                elif opcion == 5:
                    self.mostrarProductos()
                elif opcion == 6:
                    print("\nLista de Clientes:")
                    for cliente in self.clientes.values():
                        print(f"- {cliente.nombre} (Cédula: {cliente.cedula})")
                    input("\nPresione Enter para continuar...")
                elif opcion == 7:
                    print("¡Gracias por usar el sistema! Hasta luego.")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Por favor ingrese un número válido.")
