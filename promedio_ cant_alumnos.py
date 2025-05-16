cant_alumnos=int(input("ingrese la cantidad de alumnos: "))
promedio=0
notas_alumnos=0
notas=0
for x in range(0,cant_alumnos):
    cant_notas= int(input(f"ingrese la Cantidad de notas del alumno {x+1}: "))
    for i in range(0,cant_notas):
        notas+= float(input(f"ingrese la nota {i+1} del alumno {x+1}: "))
    promedio= notas/cant_notas
    notas_alumnos+=promedio
    print(f"el promedio del alumno {x+1} es:{promedio}")
    if promedio>=4:
        print(f"alumno {x+1} aprovo")
    else:
        print(f"alumno {x+1} reprovo")
    print(f"el promedio general del cuerso es: {notas_alumnos/cant_alumnos}")

