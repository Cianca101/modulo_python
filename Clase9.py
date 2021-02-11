### OBJETOS ###
class Celular(object):
    def __init__(self, marca, estado): # usuario da datos de marca y estado
        self.marca = marca
        self.estado = estado
    def llamar(self):
        self.estado = "En llamada"
        print("Llamando")
    def colgar(self):
        self.estado = "Colgando"
        print("Colgando")

mi_cel = Celular("Nokia", "ahorro")
mi_cel2 = Celular("Samsung", "cargando")

### self.i como acumulador
i = 0
class Acumulador(object):
    def __init__(self): # no pedimos valor de i, inicia en 0
        self.i = 0
    def sum(self):
        self.i += 1
        print(self.i)
    def res(self):
        self.i -= 1
        print(self.i)
    def resultado(self):
        print(self.i)
    

mi_acc = Acumulador()
mi_acc.sum()
mi_acc.resultado()


### Ejercicio 
class Producto(object):
    carrito = 0
    def __init__(self, precio_sin_iva = 100, iva = 0.16):
        self.precio_sin_iva = precio_sin_iva
        self.iva = iva
        #self.precio_con_iva = (1 + self.iva) * self.precio_sin_iva
        self.precio_con_iva = (1 + iva) * precio_sin_iva
        self.calcular_totales()
    def modificar_precio(self, precio_sin_iva): #sobreescribe precio
        self.precio_sin_iva = precio_sin_iva
        self.precio_con_iva = (1 + self.iva) * self.precio_sin_iva
        self.calcular_totales()
    def mostrar_precio_iva(self):
        print(self.precio_con_iva)
    def comprar_una_unidad(self):
        self.carrito += 1
        self.calcular_totales()
    def calcular_totales(self):
        self.subtotal = self.precio_sin_iva * self.carrito
        self.impuesto = self.iva * self.subtotal
        self.total = self.subtotal * self.impuesto
    def mostrar_totales(self):
        print(f'Unidades compradas {self.carrito}')
        print(f'Subtotal: ${self.subtotal}')
        print(f'Impuestos: ${self.impuesto}')
        print(f'Total: ${self.total}')

producto1 = Producto(200)
print(producto1.precio_sin_iva)
producto1.modificar_precio(150)
print(producto1.precio_sin_iva)
producto1.mostrar_precio_iva()
producto1.calcular_totales()
producto1.comprar_una_unidad()
producto1.mostrar_totales()

