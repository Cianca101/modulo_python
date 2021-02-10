### Crear 2 variables (2 productos) y asignarles 1 precio
producto1 = 100.0
producto2 = 200.0

### Aplicar iva (16%)
iva = 0.16
producto1_iva = producto1 * (1 + iva)
producto2_iva = producto2 * (1 + iva)

### Calcular el precio total de una pieza por producto
total_compra = producto1_iva + producto2_iva
iva_total = (producto1 * iva) + (producto2 * iva)
print("iva total: $", iva_total)
print("Total: $", total_compra)

### Calcular total, 4 unidades producto 1, 5 unidades producto 2
unidades1 = 4
unidades2 = 5
impuesto = ((producto1 * unidades1) + (producto2 * unidades2)) * iva
subtotal = (producto1 * unidades1) + (producto2 * unidades2)
total = subtotal + impuesto
print("impuestos: $", impuesto)
print("subtotal: $", subtotal)
print("total: $", total)

### Aplicar 2 operaciones con entero
numA = 10
numB = 5
resultadoSuma = numA + numB
resultadoResta = numA - numB
print("resultado suma = ",resultadoSuma)
print("resultado resta = ",resultadoResta)

### 2 Operaciones stings
nombre = "Emma Cianca"
cadena = "Mi nombre es {}"
print(cadena.format(nombre))
lista = cadena.format(nombre).split(" ")
print(lista)


### Crear una lista con nombres de 5 compañeros
l_nombres = ["Ale Paez", "Gabriela Camarillo", "Emmanuel Cianca", "Gilberto Garcia", "Liliana Juarez"]
print(l_nombres)

### Crear lista l_dato con tiempo que tardan en llegar al trabajo (o edad)
20, 0, 10, 35, 40
l_dato = [20, 0, 10, 35, 40]
print("minutos: ", l_dato)

### Cambiar el tiempo o edad del 3er compañero
#l_dato.pop(2)
#l_dato.insert(2, 30)
#print(l_dato)
# o en facil:
l_dato[2] = 30

### Mostrar compañeros con menos de 26 años
l_resultado = [l_nombres[i] for i in range(len(l_nombres)) if l_dato[i] < 26]
print(l_resultado)

### Crear lista horas de sueño promedio
l_horas = [7, 6, 6, 3, 8]
print(l_horas)

### Mostrar compañeros que duermen mas de 8 hrs
l_8hrs = [l_nombres[i] for i in range(len(l_horas)) if l_horas[i] > 8]

### Mostrar a quienes dermen menos de 8 hrs, si duermen menos de 4 hrs llamarlos vampiros
l_menos8 = [l_nombres[i] for i in range(len(l_horas)) if l_horas[i] > 8]
print(l_menos8)
l_vampiro = ["Vampiro" + ${l_nombres[i]} for i in range(len(l_horas)) if l_horas[i] < 4 ]
print(l_vampiro)

# con if
horas_suenio = 3

if horas_suenio < 4:
    print("eres un vampiro")
elif horas_suenio < 8:
    print("duermes  muy poco")
    else:
        print("que envidia")

