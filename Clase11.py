### Repaso list, diccionarios


class Lista(object):
    def __init__(self, *valores):
        self.__lista_interna = []
        for i in valores:
            self.__lista_interna.append(i)
    def __str__(self):
        aux = "["
        for i in self.__lista_interna:
            aux += str(i) + ","
        aux += "]"
        return(aux)
    def extend(self, lista):
        for i in lista:
            self.__lista_interna.append(i)
    def append(self, lista):
        self.__lista_interna.append(lista)
    def pop(self, elemento_consultado):
        self.__lista_interna = [elemento for elemento in self.__lista_interna if elemento != elemento_consultado]


### Ejercicio Vehiculos
class Transportes(object):
    def __init__(self, atributos, marca, dimensiones, capacidad):
        self.atributos = atributos
        self.marca = marca
        self.dimensiones = dimensiones
        self.capacidad = capacidad
    def desplazamiento(self):
        print(f'Atributos: {self.atributos}')
        print(f'Marca: {self.marca}')
        print(f'Dimensiones: {self.dimensiones}')
        print(f'Capacidad: {self.capacidad}')


class Terrestres(Transportes):
    def __init__(self, atributos, marca, dimensiones, capacidad, n_llantas, terreno_desplazamiento):
        super().__init__(atributos, marca, dimensiones, capacidad):
        self.n_llantas = n_llantas
        self.terreno_desplazamiento = terreno_desplazamiento
    def desplazamiento(self):
        print(f'Atributos: {self.atributos}')
        print(f'Marca: {self.marca}')
        print(f'Dimensiones: {self.dimensiones}')
        print(f'Capacidad: {self.capacidad}')
        print(f'No. LLantas: {self.n_llantas}')
        print(f'Tipo de Terreno: {self.terreno_desplazamiento}')


class Autos(Terrestres):
    def __init__(self, atributos, marca, dimensiones, capacidad, n_llantas, terreno_desplazamiento, aacc, n_rin):
        super().__init__(atributos, marca, dimensiones, capacidad, n_llantas, terreno_desplazamiento):
        self.aacc = aacc
        self.n_rin = n_rin
    def desplazamiento(self):
        print(f'Atributos: {self.atributos}')
        print(f'Marca: {self.marca}')
        print(f'Dimensiones: {self.dimensiones}')
        print(f'Capacidad: {self.capacidad}')
        print(f'No. LLantas: {self.n_llantas}')
        print(f'Tipo de Terreno: {self.terreno_desplazamiento}')
        print(f'A/C: {self.aacc}')
        print(f'No. Rin: {self.n_rin}')

### Método Polimorfismo
def mover(objeto):  # ex.- mover jeep que es Auto
    objeto.deseplazamiento() #todos en comun: desplazamiento

#Instrucciones nombrar objeto
tigre1 = Transporte
transpo = Terrestres
jeep = Autos

#Llamar polimorfismo desplazamiento
mover(tigre1)
mover(transpo)
mover(jeep)