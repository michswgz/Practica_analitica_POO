from FigurasGeometricas import FigurasGeometricas
From Triangulo import Triangulo

nombre =input("¿Que figura geometrica desea usar?")
print("La figura seleccionada es:", nombre)

#instancia clase padre
fg= FigurasGeometricas(nombre)
fg.area()

tr=Triangulo(10,20)
