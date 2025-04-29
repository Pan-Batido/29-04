numero = int(input("ingrese un número:"))
numero =numero+1
for i in range(1,numero):
    if i%2==0:
        print("par",i)
    else:
        print("impar",i)
