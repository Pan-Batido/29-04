def suma():
    n1= int(input("ingrese número:"))
    n2= int(input("ingrese otro número:"))
    print("el resultao de la suma es: ")
def resta():
    n1= int(input("ingrese número:"))
    n2= int(input("ingrese otro número:"))
    print("el resultao de la resta es: ")
def multiplicacion():
    n1= int(input("ingrese número:"))
    n2= int(input("ingrese otro número:"))
    print("el resultao de la multiplicacion es: ")
def division():
    n1= int(input("ingrese número:"))
    n2= int(input("ingrese otro número:"))
    print("el resultao de la multiplicacion es: ")
def division():
    try:
        n1=int(input("Ingrese un numero:  "))
        n2=int(input("Ingrese otro numero:  "))
        print("El resultado de la division es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        # Código para manejar la excepción
        print(f"Se produjo una excepción: {nombre_de_excepcion}")

def calcladora():
    while True:
        op=int(input('''Seleccione su opcion
                    1.- Suma
                    2.- Resta
                    3.- Multi
                    4.- Division
                    5.- Salir
                    '''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multi")
                multi()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo")
                break
            case _:
                print("Opcion Invalida")

calculadora()
