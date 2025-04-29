def listar_productos(productos):
    return productos

def obtener_producto_por_indice(productos, indice):
    if 0 <= indice < len(productos):
        return productos[indice]
    return None
