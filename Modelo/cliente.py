class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__historialCompras = []

    def agregarFactura(self, factura):
        self.__historialCompras.append(factura)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena.")
        self.__nombre = nombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        if not isinstance(cedula, str):
            raise ValueError("La cédula debe ser una cadena.")
        self.__cedula = cedula

    @property
    def historialCompras(self):
        return self.__historialCompras