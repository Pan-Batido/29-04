cant_productos=0
cant_1=0
cant_2=0
cant_3=0
cant_4=0
descuento=0
total=0
menu=True
while menu:
    
    op=int(input('''Seleccione su opcion
            1.- Pikachu Roll $4500
            2.- Otaku Roll $5000
            3.- Pulpo Venenoso Roll $5200
            4.- Anguila Eléctrica Roll $4800
            5.- Salir y pagar
            6.- Ingresar cupon
            ingrese opcion: '''))
    match op:
        case 1:
            cant=int(input("cuantos desea agregar(1,2,3 ó 4):"))
            cant_productos+=cant
            cant_1+=cant
            total+=4500*cant
        case 2:
            cant=int(input("cuantos desea agregar(1,2,3 ó 4):"))
            cant_productos+=cant
            cant_2+=cant
            total+=5000*cant
        case 3:
            cant=int(input("cuantos desea agregar(1,2,3 ó 4):"))
            cant_productos+=cant
            cant_3+=cant
            total+=5200*cant
        case 4:
            cant=int(input("cuantos desea agregar(1,2,3 ó 4):"))
            cant_productos+=cant
            cant_4+=cant
            total+=4800*cant
        case 5:
            print()
            break
        case 6:
            codigo=(input("ingrese codigo de descuento:"))
            if codigo == "soyotaku":
                print("obtubiste un 10% de descuento")
                descuento=(total*0.1)
                total_descuento= total-descuento
            else:
                print("código no válido")
        case _:
            print("elija una opcion del 1 al 4")
#while True:
    # codigo=(input("tiene codigo de descuento:"))
    # if codigo == "si":
    #     codigo=(input("ingrese codigo de descuento:"))
    #     if codigo == "soyotaku":
    #         print("obtubiste un 10% de descuento")
    #         total= total-(total*0.1)
    #     else:
    #         print("código no válido")
    # else:
    #     break
# menu= input("si desea volver al menu ingrese x: ")
# if menu== "x":
#     menu=True
# else:

if descuento>0:
    print(f'''
                ******************************
                TOTAL PRODUCTOS:{cant_productos}
                ******************************
                Pikachu Roll : {cant_1}
                Otaku Roll : {cant_2}
                Pulpo Venenoso Roll : {cant_3} 
                Anguila Eléctrica Roll : {cant_4}
                ******************************
                Subtotal por pagar: ${total}
                Descuento por código: ${total*0.1}
                TOTAL: ${total_descuento}
                    ''')
else:
    print(f'''
                ******************************
                TOTAL PRODUCTOS:{total}
                ******************************
                Pikachu Roll : {cant_1}
                Otaku Roll : {cant_2}
                Pulpo Venenoso Roll : {cant_3} 
                Anguila Eléctrica Roll : {cant_4}
                ******************************
                Subtotal por pagar: ${total}
                Descuento por código: ${0}
                TOTAL: ${total}
                    ''') 