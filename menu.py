from FigurasGeometricas import FigurasGeometricas
from Cuadrado import Cuadrado
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
fg=FigurasGeometricas

#def Menu_Funciones:
while True:
    print ("______________Opciones_______________")
    print ("1.Area cuadrado")
    print ("2.Area triangulo")
    print ("3.Area circulo")
    print ("4.Area rectangulo")
    print ("5. Salir")
    opcion= input("Selecciona una opcion: ")
    #opcion=input("Selecciona una opcion: ")

    if opcion == "1":
        lado=float(input("Ingrese un lado: "))
        cd = Cuadrado(lado)
        print("El area del cuadrado es: ", cd.area () )
    elif opcion == "2":
        base=float(input("Ingrese una base: "))
        altura=float(input("Ingrese una altura: "))
        tr = Triangulo(base,altura)
        print("El area del triangulo es: ", tr.area())
    elif opcion == "3":
        radio=float(input("Ingrese un radio: "))
        cr = Circulo(radio)
        print("El area del circulo es: ", cr.area_circulo())
    

    

    
    