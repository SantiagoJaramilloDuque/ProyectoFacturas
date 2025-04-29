from Modelo.cliente import Cliente

def crear_cliente(diccionario_clientes, nombre, cedula):
    cliente = Cliente(nombre, cedula)
    diccionario_clientes[cedula] = cliente
    return cliente

def eliminar_cliente(diccionario_clientes, cedula):
    if cedula in diccionario_clientes:
        del diccionario_clientes[cedula]
        return True
    return False

def buscar_cliente(diccionario_clientes, cedula):
    return diccionario_clientes.get(cedula)

def listar_clientes(diccionario_clientes):
    return diccionario_clientes.values()
