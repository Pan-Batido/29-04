#calves
clave_1=1133
clave_2=4466
clave_3=7799
#usuarios
usuario_1= 50000
usuario_2= 80000
usuario_3= 100000
#contador
caja_roja=30
caja_azul=30
caja_rananja=30

usuario=int(input('''ingrese su usuario:
                  usuario 1
                  usuario 2
                  usuario 3'''))

clave=int(input("ingrese clave secreta:"))

while clave_1==clave and usuario_1==usuario:
    print('''1.-5000   2.-10000
          3.-15000   4.-20000
          4.-25000   5.-30000''')
    plata=int(input("ingrese retiro"))