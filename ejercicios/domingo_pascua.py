# ## Domingo de pascua ####
# Preguntar la Cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño

import random

cant_niños= int(input("ingrese la cantidad de niños: "))
while cant_niños<0:
    print("ingrese solo nuemeros enteros")
    cant_niños= int(input("ingrese la cantidad de niños: "))

noob=0
master=0
legend=0
for i in range(cant_niños):
