############################################
### REPASO SÁBADO 13 FEBRERO ###

# Listas - Ejercicios
# 1.1 Eliminar elementos duplicados perro perro sin usar set
lista = ["perro", "gato", "conejo", "perro", "perro"]
lista2 = []

for i in lista:
    if i not in lista2:
        lista2.append(i)

# 1.2 Eliminar perro, perro usando set
lista = {"perro", "gato", "conejo", "perro", "perro"}
lista = set(lista)


# 2.1 Combinar listas sin funciones
first_list = ["M", "nom", "e", "Cia"]
second_list = ["i", "bre", "s", "nca"]
final_string = ""

for i in range(len(first_list)):
    final_string += first_list[i] + second_list[i] + " "

# 2.2 Combinar listas usando funciones


# Ejercicio 3
#input [a, b]
# n = 2
#output [a1, b1, a2, b2, ...]
# lista[i] + n(i+1)
lista = ["a", "b", "c"]
n = 2
j = 1
lista_final = []

while j <= n:
    for i in lista:
        new = i + str(j)
        lista_final.append(new) 
    j += 1

# def list_mas_num (lista,num):
#     final_list=[]
#     for j in range(1,num):
#         for i in lista:  
#             suma=i+str(j)
#             final_list.append(suma)
#     print(final_list)
#     return final_list