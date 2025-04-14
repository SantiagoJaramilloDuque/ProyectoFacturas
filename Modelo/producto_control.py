class ProductoControl:
    def __init__(self, nombre, valor, registroICA, frecuenciaAplicacion):
        self.__nombre = nombre
        self.__valor = valor
        self.__registroICA = registroICA
        self.__frecuenciaAplicacion = frecuenciaAplicacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena.")
        self.__nombre = nombre

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.__valor = valor

    @property
    def registroICA(self):
        return self.__registroICA

    @registroICA.setter
    def registroICA(self, registroICA):
        self.__registroICA = registroICA

    @property
    def frecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion

    @frecuenciaAplicacion.setter
    def frecuenciaAplicacion(self, frecuenciaAplicacion):
        self.__frecuenciaAplicacion = frecuenciaAplicacion