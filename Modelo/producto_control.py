from Modelo.producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre, valor, registroICA, frecuenciaAplicacion):
        super().__init__(nombre, valor)
        self.registroICA = registroICA
        self.frecuenciaAplicacion = frecuenciaAplicacion
