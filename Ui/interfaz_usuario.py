from Modelo.control_fertilizantes import ControlFertilizantes
from Modelo.control_plagas import ControlPlagas
from Modelo.antibiotico import Antibiotico

from Crud import cliente_crud, factura_crud, producto_crud

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
        for i, producto in enumerate(producto_crud.listar_productos(self.productosDisponibles), 1):
            print(f"{i}. {producto.nombre} - ${producto.valor}")

    def buscar_por_cedula(self, mensaje="Ingrese la cédula del cliente: "):
        cedula = input(f"\n{mensaje}")
        cliente = cliente_crud.buscar_cliente(self.clientes, cedula)
        if not cliente:
            print("\nCliente no encontrado.")
            input("Presione Enter para continuar...")
        return cliente

    def crearFactura(self, cliente):
        factura = factura_crud.crear_factura(cliente)
        while True:
            self.mostrarProductos()
            try:
                seleccion = int(input("\nSeleccione el número del producto a agregar: ")) - 1
                producto = producto_crud.obtener_producto_por_indice(self.productosDisponibles, seleccion)
                if producto:
                    factura_crud.agregar_producto_a_factura(factura, producto)
                    print(f"\nProducto '{producto.nombre}' agregado a la factura.")
                else:
                    print("\nSelección inválida.")
            except ValueError:
                print("\nPor favor ingrese un número válido.")
            
            continuar = input("¿Desea agregar otro producto? (s/n): ")
            if continuar.lower() != 's':
                break

        factura_crud.mostrar_factura(factura)
        input("Presione Enter para continuar...")

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
                    nombre = input("\nIngrese el nombre del cliente: ")
                    cedula = input("Ingrese la cédula del cliente: ")
                    cliente_crud.crear_cliente(self.clientes, nombre, cedula)
                    print(f"\nCliente '{nombre}' creado exitosamente.\n")
                    input("Presione Enter para continuar...")

                elif opcion == 2:
                    cliente = self.buscar_por_cedula()
                    if cliente:
                        self.crearFactura(cliente)

                elif opcion == 3:
                    cliente = self.buscar_por_cedula()
                    if cliente:
                        print(f"\nHistorial de compras de {cliente.nombre}:")
                        for factura in factura_crud.listar_facturas(cliente):
                            factura_crud.mostrar_factura(factura)
                        input("\nPresione Enter para continuar...")

                elif opcion == 4:
                    cliente = self.buscar_por_cedula("Ingrese la cédula del cliente a eliminar: ")
                    if cliente:
                        cliente_crud.eliminar_cliente(self.clientes, cliente.cedula)
                        print("Cliente eliminado exitosamente.")
                        input("\nPresione Enter para continuar...")

                elif opcion == 5:
                    self.mostrarProductos()

                elif opcion == 6:
                    print("\nLista de Clientes:")
                    for cliente in cliente_crud.listar_clientes(self.clientes):
                        print(f"- {cliente.nombre} (Cédula: {cliente.cedula})")
                    input("\nPresione Enter para continuar...")

                elif opcion == 7:
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

            except ValueError:
                print("Por favor ingrese un número válido.")
