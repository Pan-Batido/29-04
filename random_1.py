import random
numero_azar=random.randint(1,50)

# if numero_azar>=20:
#     print("puede pasar")
# else:
#     print("falta puntaje")

numero=int(input("ingrese un numero: "))
while numero!=numero_azar:

    nnumero=int(input("ingrese un numero: "))
    if numero>numero_azar:
        print("el nuemro a adivinar es menor")
    else:
         print("el nuemro a adivinar es mayor")
print("!!ADIVINASTE¡¡")