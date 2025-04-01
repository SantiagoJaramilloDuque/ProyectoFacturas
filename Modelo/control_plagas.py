from Modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre, valor, registroICA, frecuenciaAplicacion, periodoCarencia):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.periodoCarencia = periodoCarencia
