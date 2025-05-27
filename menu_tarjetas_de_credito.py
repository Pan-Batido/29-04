#import os,sys
while True:
    while True:
        try:
            op=int(input('''
                        seleccione una opcion
                        1.-
                        2.-
                        3.- Salir
                        '''))
            break
        except Exception:
            print("solo numeros enteros")
    match op:
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            print("saliendo")
            break
        case _:
            print("opcion invalida")
        

