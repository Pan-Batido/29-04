# Designe 2 cantdidatos. Pregunte cuanto votantes son
# por cada votante , debe peguntar por quin votrá
# cuente la cantidad de votos y muestre los resultados
# definir quien ganó la votacion. Considere empate

numero_votantes= int(input("ingrese un numero de votantes: "))

zelda=0
ganondorf=0

for i in range(numero_votantes):
    voto=0
    while voto!=1 and voto!=2:   
        print("1.-Zelda  2.-Ganonorf")
        voto=int(input("ingrese su voto: "))
        if voto==1:
            zelda+=1
        elif voto==2:
            ganondorf+=1
        else:
            print("Error, selecione un voto válido")

print("los votos de Zelda son", zelda)
print("los votos de Ganondorf son", ganondorf)

if zelda>ganondorf:
    print("Zelda gano")
elif zelda<ganondorf:
    print("Ganondorf gano")
else:
    print("es empate")