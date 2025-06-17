#'''realize una funcion que calcule el iva'''

# def cal_iva (n):
#     return n*0.19

# def cal_desc (precio,porc):
#     return precio(porc/100)

# productos=[
#     {'nombre':'lapiz', 'precio':400},
#     {'nombre':'goma', 'precio':300},
#     {'nombre':'esruche', 'precio':1600}
# ]

# print(productos[1][])

'''el articulo lapiz'''

# for item in productos:
#     print(f'el atriculo{item['nombre']} tiene un prcio de{item['precio']}')

'''
1.- Agrega articulo y precios
2.- Borrar articulos
3.- Actualizar articulos
4.- mostrar lista de articulos
5.- salir
'''

articulos=[]

while True:
    
    print('''
        1.- Agrega articulo
        2.- Borrar articulos
        3.- Actualizar articulos
        4.- mostrar lista de articulos
        5.- salir
        ''')
    op=int(input('ingrese una opción:'))

    match op:
        case 1:
            nombre= input('ingrese el nombre del articulo: ')
            precio= int(input('ingrese el precio: '))
            articulos.append({'nombre':nombre,'precio':precio})
        case 2:
            for i,producto in enumerate(articulos):
                    print(i+1, ".-", articulos['nombre'], "- $", articulos['precio'])
            if len(articulos) == 0:
                print('No hay articulos para borrar')
            else:
                sel=int(input("Seleccione un articulo a borrar: "))
                print("Usted selecciono el articulo ", articulos[sel-1])
                articulos.pop(sel-1)
        case 3:
            for i,producto in enumerate(articulos):
                    print(i+1, ".-", articulos['nombre'], "- $", articulos['precio'])
            if len(articulos) == 0:
                print('No hay articulos para actualizar')
            else:
                sel=int(input("Seleccione un articulo a actualizar: "))
                print("Usted selecciono el articulo ", articulos[sel-1])
                nombre= input('ingrese el nuevo nombre del articulo: ')
                precio= int(input('ingrese el nuevo precio: '))
                articulos[sel-1] = {'nombre':nombre,'precio':precio}
        case 4: 
            print(articulos)
        case 5:
            print("Saliendo")
            break