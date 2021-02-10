### Funciones
#Ejercicio Calculadora
def nombre_funcion(parametros):
    codigo
    exit

def suma(x, y):
    return(x + y)

def resta(x, y):
    return(x - y)

def mult(x, y):
    return(x * y)

def div(x, y):
    if y == 0:
        print("No puedes dividir entre cero")
        return None
    return(x / y)

def calculadora(x, y, operacion):
    if operacion == "suma":
        return(suma(x, y))
    if operacion == "resta":
        return(resta(x, y))
    if operacion == "mult":
        return(mult(x, y))
    if operacion == "div":
        return(div(x, y))
    


#################################################
#Ejercicio
# crear funcion que recibe:
    # precio de producto sin iva como lista
    # cuantos productos se compran como lista
    # subtotal = suma (precio sin iva[i] * cantidad [i] para cada i en la lista)
    # impuesto = suma (precio sin iva[i] * cantidad [i] para cada i en la lista) * iva
    # total = subtotal + impuesto
    # Calcular subtotal, total...regresar data

l_producto = {"manzana", "carne", "huevo", "leche"}
l_cant = {20, 1, 18, 6}
l_precio = {20, 89, 22, 17}
iva = 0.16

for precio in range(len(l_precio)):
    print(l_precio[i])

for precio, cantidad in zip(l_precio, l_cant):
    print(precio, cantidad)


### Factorial 1 al 9
resultado = 1

for i in [j for j in range(1, 10)]:
    resultado *= i

print(resultado)

### Factorial 1 al n de otra manera
def factorial(n):
    if n == 1:
        return(1)
    else:
        return(n * factorial(n - 1))

