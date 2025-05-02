arancel = 200000
descuento=0
print('''
      1.-la florida 20%
      2.-la pintada 30%
      3.-puente alto 25%
      4.-san joaquin 15%''')

comuna=int(input("introduzca su comuna: "))
if comuna==1:
    descuento+=0.2
elif comuna==2:
    descuento+=0.3
elif comuna==3:
    descuento+=0.25
elif comuna==4:
    descuento+=0.15
else:
    print("comuna invalida")

cantidad_personas= int(input("introduzca cantiadad de personas: "))
if cantidad_personas==1:
    descuento=0.02
elif cantidad_personas>=2 and cantidad_personas<=4:
    descuento=0.03
elif cantidad_personas>=5:
    descuento=0.04
else:
    print("invalida")

arancel_total= arancel-(arancel*descuento)

print("el total a pagar es,",arancel_total)
