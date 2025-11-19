from FigurasGeometricas import FigurasGeometricas
from Cuadrado import Cuadrado
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma
from Trapecio import Trapecio
from Rombo import Rombo
fg=FigurasGeometricas

#def Menu_Funciones:
while True:
    print ("______________Opciones_______________")
    print ("1.Area cuadrado")
    print ("2.Area triangulo")
    print ("3.Area circulo")
    print ("4.Area rectangulo")
    print("5.Area cilindro")
    print("6.Area paralelograma")
    print("7.Trapecio")
    print("8.Rombo")
    print ("9. Salir")
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
    elif opcion == "4":
        largo=float(input("Ingrese un largo: "))
        ancho=float(input("Ingrese un ancho: "))
        rc = Rectangulo(largo, ancho)
        print("El area del rectangulo es: ", rc.area_rectangulo())
    elif opcion == "5":
        altura=float(input("Ingrese una altura: ")) 
        radio=float(input("Ingrese un radio: "))
        cl = Cilindro("cilindro")
        cl.altura = altura
        cl.radio = radio
        print("El area del cilindro es: ", cl.area_cilindro())
    elif opcion == "6":
        altura=float(input("Ingrese una altura: ")) 
        base=float(input("Ingrese una base: "))
        para = Paralelograma ("Paralelograma")
        para.altura = altura
        para.base = base
        print("El area del paralelograma es: ", para.area())
    elif opcion == "7":
        basemayor=float(input("Ingrese una base mayor: "))
        basemenor=float(input("Ingrese una base menor: "))
        Altura=float(input("Ingrese una altura: "))
        tra = Trapecio("Trapecio")
        tra.baseMayor = basemayor
        tra.baseMenor = basemenor
        tra.altura = Altura 
        print("El area del trapecio es: ", tra.area())
    elif opcion == "8":
        diagonalmayor=float(input("Ingrese un diagonal mayor: "))
        diagonalmenor=float(input("Ingrese una diagonal menor: "))
        rm = Rombo("Rombo")
        rm.diagonalMayor = diagonalmayor
        rm.diagonalMenor = diagonalmenor
        print("El area del rombo es: ", rm.area())
    elif opcion == "9":
        print("Saliendo del programa...")
        break

    

    
    