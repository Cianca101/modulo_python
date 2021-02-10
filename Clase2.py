### String y Methods

### Recordatorio, Python no tiene i++, pero...
print("inicializando i con valor 1")
i = 1
print("sumamos + 1")
i += 1
print("Resultado = ", i)
# print("Resultado = " + str(i))

texto_resultado = "El resultado es: {}"
print(texto_resultado.format(i))

texto_resultado = texto_resultado.format(i)
print(texto_resultado)

### F-Strings
nombre = "Emma"
apellido = "Cianca"

print(f"Bienvenido {nombre} {apellido}")

# Publicidad Empresa
nombre_empresa = "EnfermerApp"
publicidad = """ Plataforma educativa
para estudiantes de enfefrmeria """

mi_empresa = """Mi empresa es {}
y se dedica a {}"""

print(mi_empresa.format(nombre_empresa, publicidad))


### Funciones type, len
print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("True es un bool", type(True))
print("3.333 es un float", type(3.333))

#len
len("Hola...")

### Obtener Caracteres
frase = "Hola Mundo"
print(frase[1]) #obtener elemento 1, o
print(frase[len(frase) - 1]) #obtener ultimo elemento
print(frase[-1]) #obtener ultimo elemento en reversa
print(frase[0 : 3]) # obtener elementos del 0 al 2,
#se queda en limite - 1
#(inicio : final : tamaño del salto)
# final se queda en final-1 

### Metodos String
#.find
#.lower
#.upper
#.swapcase
#.relpace
#.split
datos = "12 | 13 | 14"
col1, col2, col3 = datos.split("|")
print(col1, col2, col3)
#.join
lista_col = datos.split("|")
"|".join(lista_col)