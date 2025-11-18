from FigurasGeometricas import FigurasGeometricas
class Rectangulo(FigurasGeometricas):
    def ___init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura 