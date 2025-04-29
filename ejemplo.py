edad=-1
while edad<0 or edad>100:
    edad= int(input("ingrese edad:"))
    if edad<0 or edad>100:
        print("ingrese una edad entre 0 y 100")

print("ingreso la edad exitosamente")