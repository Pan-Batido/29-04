numero= False
suma_numeros=0
contador_numeros=0

while numero!=True:
    numero=int(input("ingrese un numero: [0.- salir]"))

    if numero==0:
        numero=True
        break
    else:
        suma_numeros+= numero
        contador_numeros+= 1

print("se sumaron",contador_numeros,"nuemros")
print("la suma de todos lo números es:",suma_numeros)