'''
Crear programa de manejo de notas
1.- Ingresar nota
2.- Borrar nota
3.- Mostar notas
4.- Sacar promedio, nota mayor y nota menor
5.- Limpiar todas las notas
6.- Salir
'''

notas=[2.4, 5.8, 6.9, 7.0]
#       0    1    2    3
# for nota in notas:
#     print(nota)

# for i,nota in enumerate(notas):
#     print(i+1, ".-", nota)

# sel=int(input("seleccione una nota"))

# print("Usted selecciono  la nota ", notas[sel-1])


while True:
    while True:
        try:
            print('''
                1.- Ingresar nota
                2.- Borrar nota
                3.- Mostar notas
                4.- Sacar promedio, nota mayor y nota menor
                5.- Limpiar todas las notas
                6.- Salir
                ''')
            op=int(input("Seleccione una opción: "))
            while op<1:
                op=int(input("Seleccione una opción valida: "))
        except Exception:
            print("introduzca un numero entero")

        match op:
            case 1:
                grade=float(input("Ingrese una nota: "))
                notas.append(grade)
            case 2:
                for i,nota in enumerate(notas):
                    print(i+1, ".-", nota)
                sel=int(input("Seleccione una nota a borrar: "))
                print("Usted selecciono  la nota ", notas[sel-1])
                notas.pop(sel-1)
            case 3:
                print (notas)
            case 4:
                promedio = sum(notas)/len(notas)
                print("EL promedio es ", promedio)
                print("La nota mayor es ", max(notas))
                print("La nota menor es ", min(notas))
            case 5:
                notas.clear()
                print(f"La lista ahora cuenta con {lend(notas)}, datos")
            case 6:
                print("Saliendo")
                break
            case _:
                print("Introduzca una opción valida")
