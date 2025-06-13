#conjunto de pares de datos

# dic={
# #     key      value
#     'nombre' : 'oda',
#     'numero' : 976586939,
#     'casado' : True
# }

# print(dic)

# for key,value in dic.items():
#     print(key, value)
# dic['ciudad']='talca'

# for key,value in dic.items():
#     print(key, value)

# dic['casado']=False

# for key,value in dic.items():
#     print(key, value)

# '''ejercicio'''

frutas={
    'sandia' : 3000,
    'manzana' : 1500,
    'naranja' : 1000
}

while True:
    while True:
        try:
            print('''
                1.- Ingresar frutas y precios
                2.- Actualizar precios
                3.- Borrar frutas y precio
                4.- Mostar frutas y precio
                5.- Comprar
                6.- Salir
                ''')
            op=int(input("Seleccione una opción: "))
            while op<1 and op>6:
                op=int(input("Seleccione una opción valida: "))
        except ValueError:
            print("introduzca un numero entero")

        match op:
            case 1:
                fruta=input('ingrese una fruta: ')
                precio=int(input('ingrese precio: '))
                frutas[fruta]= precio
            case 2:
                for key,value in frutas.items():
                    print(f'{key, value}')
                sel=int(input("Seleccione una fruta: "))
                price=int(input('Introduzca el nuevo precio: '))
                frutas[fruta]= price
            case 3:
                for i,fruta in enumerate(frutas):
                    print(i+1, ".-", frutas)
                sel=int(input("Seleccione una nota a borrar: "))
                print("Usted selecciono  la fruta ", frutas[sel-1])
                frutas.pop(sel-1)
            case 4:
                print(frutas)
            # case 5:
            # case 6:
            #     print("Saliendo")
            #     break





