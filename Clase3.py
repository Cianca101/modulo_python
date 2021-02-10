### Listas
mi_primera_lista = [1, 3.1416, "HolaMundo"]

###Asigna referencia a Y
x = [1,2] #crea variable x
y = x # y es igual a x, misma cajita, mismo espacio de memoria
x[0] = 0 # x = [0 , 2]
y   #imprime y, que ahora es [0,2]
# si afecto a y, tambien afecto a x...mimo objeto distinto nombre

### Asigna valor a Y
x = [1,2]
y = x.copy() # y es igual a este momento de x
x[0] = 0 # x cambia de valor, pero y no x = [0,2]
y # y = [1,2]
# si modifico y, x no se modifica

### append
lista_1 = [1,2,3] #lista 1
lista_2 = [1,3] # lista 2
lista_1.append(lista_2) #metodo append a lista 1,
# fusiona lista2 en nuevo ultimo espacio de lista 1
lista_1 # lista_1 = [1,2,3,[1,3]]

### extend
lista_1 = [1,2,3] #lista 1
lista_2 = [1,3] # lista 2
lista_1.extend(lista_2) #metodo extend a lista 1,
# fusiona lista2 asignando un espacio a cada elemento
lista_1 # lista_1 = [1,2,3,1,3]

### remove
lista_1 = [1,2,3,3,2,1] #lista 1
lista_1.remove(2) # elimina el primer elemento que coincida
lista_1 # lista_1 = [1,3,3,2,1] eliminó el primer 2

### eliminar elemento de lista en una lista
lista_1 = [1,2,3,[1,3]] #lista 1
lista_1[3].remove(1)    # elimina el primer 1 de la sublista
lista_1     # lista_1 = [1,2,3,[3]]

### index
lista_1 = [1,2,3] #lista1
lista_2 = [1,3]   #lista2
lista_1.append(lista_2) #fusiona listas lista_1=[1,2,3,[1,3]]
lista_1.index(3) #busca el no. 3 y regresa la posición del primero que encuentre = 2

### count
lista_1 = [1,2,3,[1,3],3] #lista 1
lista_1.count(3) #cuenta cuantas veces hay un no 3
#resultado = 2

### reverse
lista_1 = [1,2,3] # lista 1
lista_1.reverse() #invierte lista_reverse = [3,2,1]

    #ejercicio reverse invertido
lista_1 = [1, 2, 3, [1, 3], 3]
lista_invertida = lista_1[::-1]
lista_reverse = lista_invertida.reverse()
print(lista_reverse)

### insert
lista_1 = [1,2,3]
lista_1.insert(2,"texto") #enla posicion 2 introduce nuuevo elemento
# resultado lista_1 = [1,2,"texto",3]

### pop
lista_1 = [1,2,3]
lista_1.pop(2) # expula el elemento de la posición no2 = 3
# resultado, lista_1 = [1,2] se expulsa 3
# #puede ser guardado en nuva variable n_pop=lista_1.pop(2) = 3

### sort
lista_1 = [1,5,2,4,3,6]
lista_1.sort() #acomoda en orden lista_1
# resultado lista_1 = [1,2,3,4,5,6]

### indices
# [inicio : (fin + 1) : salto]
x = [1,2,3,4,5]
x[::] #todos los elementos
x[1::] #del elemento 1 al len(x)-1
x[1:len(x):] #del elemento 1 al len(x)-1

x[len(x) - 1] # ultimo elemento
x[-1] # ultimo elemento
x[len(x):len(x)] # ultimo elemento
x[::-1][0] # ultimo elemento

# del

### for en listas
for i in range(10): #range(n), cuenta de 0 a n-1
    print(i)    #imprime i, desde 0 hasta 9 = n-1
    #pass    #hacer nada pero permite funcionamiento de for

lista_for = [i for i in range(100)] # crea lista con range, 100 elementos, de 0 a 99

### if en listas
[i for i in range(100) if i % 2 == 0] #lista numero pares
[i for i in range(100) if i % 2 != 0] #lista numero impares

### else en listas
[i if i % 2 == 0 else "No es par" for i in range(100)]

### Ejercicio Ruben, lista 100 elementos, lista 2 solo primeros 50 elementos
[i for i in range(100) if i in i<50]
#si es par, escribir "no es impar", else escribir i
["No es impar" if i % 2 == 0 else i for i in range(100) if i in i < 50]
