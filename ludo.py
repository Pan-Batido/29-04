import random


meta=30
turno=1
j1=0
j2=0

while j1<meta and j2<meta:
    if turno%2==0:
        print("turno juador 1")
        dado=random.randint(1,6)
        j1+=dado
    else:
        print("turno juador 2")
        dado=random.randint(1,6)
        j2+=dado
    turno+=1

if j1>j2:
    print("el ganador es juegador 1")
else:
    print("el ganador es juegador 1")

    