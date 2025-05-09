# Designe 2 peleadores solicitando sus nombres
# cada peleador tiene 50 HP, debe mostrar la barra de energia.
# Las peleas son por turnos #print("[]"*20)
# cada turno el peleador ataca entre 3 y 15
# Existe posibilidad de ataque critico del 20% sera atk*2
# gana el que le quita todo el HP al rival

import random
import time
#solicitud nombres
print("eligan sus nombres")
nombre_jugador_1=input("nombre jugador 1: ")
nombre_jugador_2=input("nombre jugador 2: ")

#vida jugadores
jugador_1=50
jugador_2=50

#pelea por turnos y ataques
turno=0
while jugador_1>0 and jugador_2>0:

    if turno%2==0:
        posibilidad=random.randint(1,5)
        ataque=random.randint(3,5)
        print("turno jugador 1")
        if posibilidad==1:
            jugador_2-=ataque*2
        else:
            jugador_2-=ataque
        print(nombre_jugador_1)
        print("▄"*jugador_1,jugador_1,"HP")
        print(nombre_jugador_2)
        print("▄"*jugador_2,jugador_2,"HP")
        turno+=1
        time.sleep(1)
    else:
        posibilidad=random.randint(1,5)
        ataque=random.randint(3,5)
        print("turno jugador 2")
        if posibilidad==1:
            jugador_1-=ataque*2
        else:
            jugador_1-=ataque
        print(nombre_jugador_1)
        print("▄"*jugador_1,jugador_1,"HP")
        print(nombre_jugador_2)
        print("▄"*jugador_2,jugador_2,"HP")
        turno+=1
        time.sleep(1)

if jugador_1>jugador_2:
    print(nombre_jugador_1,"gana!!")
else:
    print(nombre_jugador_2,"gana!!")