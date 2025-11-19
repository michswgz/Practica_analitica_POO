from FigurasGeometricas import FigurasGeometricas
from math import pi
class Cilindro(FigurasGeometricas):
    def _init_(self, nombre):
        super()._init_(nombre)

    @property
    def radio(self):
        return self._radio
    @radio.setter
    def radio(self, radio: float):
        self._radio=radio
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, altura: float):
        self._altura=altura

    def area_cilindro(self):
        return 2 * pi * self.radio*(self.radio * self.altura)