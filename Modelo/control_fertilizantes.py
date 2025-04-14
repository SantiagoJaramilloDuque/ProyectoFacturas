from Modelo.producto_control import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, nombre, valor, registroICA, frecuenciaAplicacion, fechaUltimaAplicacion):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.__fechaUltimaAplicacion = fechaUltimaAplicacion

    @property
    def fechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion

    @fechaUltimaAplicacion.setter
    def fechaUltimaAplicacion(self, fechaUltimaAplicacion):
        self.__fechaUltimaAplicacion = fechaUltimaAplicacion