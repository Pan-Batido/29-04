def boleta():
    print(f"Hola {nombre_usuario}")
    print(f"Cantidad de productos: {cant_productos}")
    print(f"Total neto{total}")
    print(f"Total iva incluido:{(total*0.19)+total}")

cant_productos=0
total=0
nombre_usuario=input("ingrese su nombre: ")

while True:
    op=int(input('''Seleccione su opcion
                1.- ingresar nombre
                2.- comprar
                3.- generar boleta
                4.- Salir
                ingrese opcion: '''))
    match op:
        case 1:
            nombre_usuario=input("ingrese su nombre: ")
        case 2:
            while True:
                op=int(input('''Seleccione su opcion
                    1.- queque $3.000
                    2.- mendoino $1.500
                    3.- kuchen $8.500
                    4.- pie limon $8.500
                    5.- Salir
                    ingrese opcion: '''))
                match op:
                    case 1:
                        print()
                        cant_productos+=1
                        total+=3000
                    case 2:
                        print()
                        cant_productos+=1
                        total+=1500
                    case 3:
                        print()
                        cant_productos+=1
                        total+=8500
                    case 4:
                        print()
                        cant_productos+=1
                        total+=8500
                    case 5:
                        print()
                        break
                    # case _:
                    #     print("Opcion Invalida")
                    boleta()
