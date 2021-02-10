# con if
horas_suenio = 3

if horas_suenio < 4:
    print("eres un vampiro")
elif horas_suenio < 8:
    print("duermes  muy poco")
else:
    print("que envidia")

###
edad_cliente = 27
nombre_cliente = "Fulanito"
compras_mensuales = 13000

if 18 >= edad_cliente >= 0 and compras_mensuales >= 10000:
    print(nombre_cliente, "es junior")
elif 18 >= edad_cliente >= 0 and compras_mensuales <= 10000:
    print(nombre_cliente, "es pobristar")
elif 60 >= edad_cliente >= 18 and compras_mensuales >= 10000:
    print(nombre_cliente, "es fifi")
elif 60 >= edad_cliente >= 18 and compras_mensuales <= 10000:
    print(nombre_cliente, "es chairo")
elif 60 <= edad_cliente and compras_mensuales >= 10000:
    print(nombre_cliente, "es aficionado")
elif 60 <= edad_cliente and compras_mensuales <= 10000:
    print(nombre_cliente, "es peje")
elif 60 <= edad_cliente and compras_mensuales >= 50000:
    print(nombre_cliente, "es Chava JR")
elif 60 <= edad_cliente and compras_mensuales <= 50000:
    print(nombre_cliente, "es abuelito favorito")

### Otra Forma
edad2 = 63
cliente2 = "Fulanito"
compras2 = 20000

if edad2 >= 60 and compras2 > 50000:
    print(cliente2, "es Abuelo Favorito")
elif edad2 >= 60:
    print(cliente2, "es pejes")
elif compras2 > 50000:
    print(cliente2, "es Chava JR")
elif edad2 >= 18 and compras2 > 10000:
    print(cliente2, "es fifi")
elif edad2 >= 18:
    print(cliente2, "es chairos")
elif edad2 < 18 and compras2 > 10000:
    print(cliente2, "es juniors")
elif edad2 < 18:
    print(cliente2, "es aficionados")

### For
# Precio acciones
precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140 ]
a = 0
prom = 0

for i in range(len(precio_diario_promedio)):
    a += precio_diario_promedio[i]

prom = a / len(precio_diario_promedio)
print("Promedio precio acciones: $", prom)

precio_100 = precio_diario_promedio.count(100)
print("Coincidencias con 100 es: ", precio_100)


### Set (Conjuntos)
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

# Union
A | B #Fusiona A y B = {1,2,3,4,5,6}

# Intersección
A & B #Elementos coincidentes = {3,4}

#Diferencia
A - B #Elementos que estan en A y no en B = {1,2}
B - A #Elementos que estan en B y no en A = {5,6}

#Diferencia Simetrica
A ^ B #(Elementos que estan en A y no en B) unión
      #(elementos que estan en B y no en A) = {1,2,5,6}

#Subconjunto
A <= B #A es subconjunto de B? = True/False
A >= B #A es superconjunto de B? = True/False

## Metodos Set
#add - agregar elemento
A.add(100)
# A.add(11,12,13) --> ERROR

#update - agregar multiples elementos
A.update([11,12,100])

#remove - eliminar elemento determinado
A.remove(100) #en caso no encontrarlo, manda error

#discard - eliminación forzada, no manda error si no encuentra
A.discard(12)

#pop - eliminar elemento de manera aleatoria
A.pop()

#clear - elimina todos los elementos del Set
A.clear()

#############################

### Diccionarios
l_nombres2 = ["Ale Paez", "Gabriela Camarillo", "Emmanuel Cianca", "Gilberto Garcia", "Liliana Juarez"]
l_horas = [7, 6, 6, 3, 8]
l_dato2 = [20, 0, 10, 35, 40]

ejemplo1 = {
    'Ale Paez':{
        'Horas de Sueño':7,
        'Minutos al trabajo':20,
    }
}

horas_suenio_dict = {
    'Ale Paez': 7,
    'Gabriela Camarillo': 6,
    'Emma Cianca': 6,
    'Gil': 3,
    'Liliana': 8,
}

for llave, valor in horas_suenio_dict.items():
    print(f'{llave} duerme {valor}')

list(horas_suenio_dict.keys())  # Si se necesita tener las llaves como listas

for llave in horas_suenio_dict.keys():
    print(f'{llave} duerme {horas_suenio_dict[llave]}')

for valor in horas_suenio_dict.values():
    print(valor)
    promedio_horas += valor

print("Promedio de horas de sueño: ", promedio_horas/len(horas_suenio_dict.values()))

# @ Emma Ejercicio
l_nombres2 = ["Ale Paez", "Gabriela Camarillo", "Emmanuel Cianca", "Gilberto Garcia", "Liliana Juarez"]
l_horas = [7, 6, 6, 3, 8]

dict_ejercicio = {}

for i, j in zip(l_nombres2, l_horas):
    dict_ejercicio.update({i: j})
    # dict_ejercicio.setdefault(i, j)
    # dict_ejercicio[i] = j
    print(f'{i} duerme {j} horas')



### Ejercicio
#Pedir al usuario el nombre del alumno y los minutos
#que tarda a su trabajo.
#Guardarlo en diccionario, los nombres son las llaves
#y los minutos son valores, en enteros.
#El BREAK es con un unput "NO" en el nombre del alumno
#Imprime el resultado de forma agradable

in_nombre_alumno = input("Nombre del Alumno (NO = fin): ")
in_tiempo_alumno = input("Tiempo al trabajo?: ")
alumnos_dict = {}
nombre_alumno = []
tiempo_alumno = []


nombre_alumno.update([in_nombre_alumno])
tiempo_alumno.update([in_tiempo_alumno])

for i, j in (nombre_alumno, tiempo_alumno):
    alumnos_dict.update({i: j})
    print(f'{i} hace {j} minutos al trabajo')

