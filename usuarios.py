calular=int(input("ingrese su nuemro de celular: "))
print(calular[0])

usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None

#while (user== usuario1 and passw==contrasena1) or(user== usuario2 and passw==contrasena2) or (user== usuario3 and passw==contrasena3):
if usuario1==None and usuario2==None and usuario3==None:
    print("debe tener al menos un usuario")
else:
    user=input("ingrese su usuario:")
    passw=input("ingrese contraseña")
    if (user== usuario1 and passw==contrasena1) or(user== usuario2 and passw==contrasena2) or (user== usuario3 and passw==contrasena3):
        op=int(input('''ingrese una opcion:
                    1.- Realizar llamada
                    2.- Enviar correo electrónico
                    3.- Cerrar sesión
                    '''))
        match op:
            case 1:
                calular=int(input("ingrese su nuemro de celular: "))
                # print(calular[0])
                for n in calular:
                    if n==9:
                        break  
            case 2:
            case 3:
                print()
            case _:
                print("ingrese una opcion valida")