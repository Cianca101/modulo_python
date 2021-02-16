###
# Crear Clase Hogar con 3 metodos y 3 atributos
# atributo no cuartos, superficie m2, no baños
class Hogar():
    def __init__(self, num_cuartos, superficie_m2, num_baños):
        self.num_cuartos = num_cuartos
        self.superficie_m2 = superficie_m2
        self.num_baños = num_baños
    def __add__(self, casa2):
        cuartos = self.num_cuartos + casa2.num_cuartos
        print(f'No. de Cuartos en {casa1} y en {casa2}: {cuartos}')
    def status(self):
        print(f'No. de Cuartos: {self.num_cuartos}')
        print(f'Superficie en m2: {self.superficie_m2}')
        print(f'No. de Baños: {self.num_baños}')

# Crear clase departamento, hereda la clase hogar, 3 metodos y 3 atributos
# renta, mantenimiento, cocina integral (T/F)
class Departamento():
    def __init__(self, num_cuartos, superficie_m2, num_baños, renta, manteimiento, piso):
        super().__init__(num_cuartos, superficie_m2, num_baños):
        self.renta = renta
        self.manteimiento = manteimiento
        self.piso = piso
    def __len__(self):
        return(self.superficie_m2)
    def status(self):
        print(f'No. de Cuartos: {self.num_cuartos}')
        print(f'Superficie en m2: {self.superficie_m2}')
        print(f'No. de Baños: {self.num_baños}')
        print(f'Renta: {self.renta}')
        print(f'Mantenimiento: {self.manteimiento}')
        print(f'Renta Total (Renta + Mantenimiento): {self.renta + self.manteimiento}')
        print(f'No. de Piso: {self.piso}')

#utilizar __add__ en hogar que sume cuartos de la casa o depa
# casa1 +  depa1 = numero cuartos
#utilizar __len__ para devolver dimensiones de casa o depa
# len(casa1) = m2 de casa1


### Tarea: Buscar la representación oficial de una clase en un string

### try / except
# 10/0
try:
    x = 10 / 0
except:
    print("No se puede dividir entre cero!!!")

# lista = [1,2,3,4,5]
# lista[10]
try:
    lista = [1,2,3,4,5]
    lista[10]
except:
    print("No existe el Index deseado")

# colores = {rojo, verde, negro}
# colores{blanco}

# resultado 15 + "20"

# finally
error = True
try:
    x = 1
    x = x / 0
    error = False
except ZeroDivisionError:
    print("Div entre Cero")
else:
    x = x ** 2
finally:
    if not error:
        del x
