from Modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre, valor, registroICA, frecuenciaAplicacion, periodoCarencia):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia

    @periodoCarencia.setter
    def periodoCarencia(self, periodoCarencia):
        self.__periodoCarencia = periodoCarencia