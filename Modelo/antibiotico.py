from Modelo.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre, valor, dosis, tipoAnimal):
        super().__init__(nombre, valor)
        self.dosis = dosis
        self.tipoAnimal = tipoAnimal
