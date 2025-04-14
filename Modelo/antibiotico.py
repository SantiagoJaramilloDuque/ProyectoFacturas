class Antibiotico:
    def __init__(self, nombre, valor, dosis, tipoAnimal):
        self.__nombre = nombre
        self.__valor = valor
        self.__dosis = dosis
        self.__tipoAnimal = tipoAnimal

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
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
        if dosis < 0:
            raise ValueError("La dosis no puede ser negativa.")
        self.__dosis = dosis

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal