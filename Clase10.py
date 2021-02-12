### Repaso
# Crear clase AparatoElectronico
    #encendido: t, f
    #marca: Android, Apple
    #tamaño: sml, med, lrg
    #estado general: funciona, no funciona (true, fasle)

    #encender- afecta encendido
    #apagar- afecta encendido
    #descomponer- afecta estado general
    #componer- afecta estado general

class Aparato(object):
    def __init__(self, marca, dimensiones, encendido = True, funciona = True):
        self.marca = marca
        self.dimensiones = dimensiones
        self.encendido = encendido
        self.funciona = funciona
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
    def componer(self):
        self.funciona = True
    def descomponer(self):
        self.funciona = False
    def status(self):
        print(f'Marca: {self.marca}')
        print(f'Tamaño: {self.dimensiones}')
        print(f'Encendido: {self.encendido}')
        print(f'Funciona: {self.funciona}')

#####
#Crear clase Telefono
    #encendido
    #marca
    #dimensiones
    #estado general
    #estado teclas (t,f)

    #encender- afecta encendido
    #apagar- afecta encendido
    #descomponer- afecta estado general
    #componer- afecta estado general

class Telefono(object):
    def __init__(self, marca, dimensiones, funciona, teclas):
        self.marca = marca
        self.dimensiones = dimensiones
        self.encendido = encendido
        self.funciona = funciona
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
    def componer(self):
        self.funciona = True
    def descomponer(self):
        self.funciona = False
    def teclas(self):
        self.teclas = True
    def teclas(self):
        self.teclas = False
    def status(self):
        print(f'Marca: {self.marca}')
        print(f'Tamaño: {self.dimensiones}')
        print(f'Encendido: {self.encendido}')
        print(f'Funciona: {self.funciona}')
        print(f'Estado Teclas: {self.teclas}')

#crear clase celular
    #estado wifi
    #estado red gsm

    #conectar (red = {wifi, gsm})
    #desconectar
    #realizar llamada
    #colgar
    # tomar_foto

class Celular(object):
    def __init__(self, marca, funciona, wifi, gsm, camara):
        self.marca = marca
        self.estado = estado
        self.red = red
        self.camara = camara
    def componer(self):
        self.funciona = True
    def descomponer(self):
        self.funciona = False
    def wifi(self):
        self.wifi = True
        self.gsm = False
    def gsm(self):
        self.wifi = False
        self.gsm = True
    def red(self):
        self.wifi = wifi
        self.gsm = gsm
    def camara(self):
        self.camara = True
    def status(self):
        print(f'Marca: {self.marca}')
        print(f'Funciona: {self.funciona}')
        print(f'Red: {self.red}')
        print(f'camara: {self.camara}')
    
#################################################
### Ejercicio Emma ###

class Telefono(object):
    def __init__(self, marca, dimensiones, funciona, teclas):
        self.__marca = marca
        self.__dimensiones = dimensiones
        self.__encendido = True
        self.__funciona = funciona
        self.__teclas = teclas
    def encender(self):
        self.__encendido = True
    def apagar(self):
        self.__encendido = False
    def componer(self):
        self.__funciona = True
    def descomponer(self):
        self.__funciona = False
    def componer_teclas(self):
        self.__teclas = True
    def descomponer_teclas(self):
        self.__teclas = False
    def status(self):
        print(f'Marca: {self.__marca}')
        print(f'Tamaño: {self.__dimensiones}')
        print(f'Encendido: {self.__encendido}')
        print(f'Funciona: {self.__funciona}')
        print(f'Estado Teclas: {self.__teclas}')

    
