from FigurasGeometricas import FigurasGeometricas
class Cuadrado(FigurasGeometricas):
    def ___init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado*self.lado