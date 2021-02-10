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
    

