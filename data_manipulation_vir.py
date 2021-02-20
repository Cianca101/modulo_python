### Ejercicio 1
n = input("Número a multiplicar (1-10): ")

# if n >= 1 and n <= 10:
#     for i in range(1, 11):
#         resultado = n * i
#         print(f'{n} x {i} = {resultado}')  
# else:
#     print("Número fuera de rango")

if n >= 1 and n <= 10:
    for i in range(1, 11):
      resultado = n * i
      print(f'{n} x {i} = {resultado}') 
else:
    print("Número fuera de rango")

