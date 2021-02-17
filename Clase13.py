########################
## Crear Paquetes
# Carpeta code
# Carpeta paquete
# archivo __init__.py

# Importar Paquetes 
# (en terminal, abrir interprete
# un nivel arriba del paquete)
import paquete
paquete.suma(4,1) == 5

### La mejor manera
import paquete as pkg
pkg.suma(5,3) === 8

from paquete import suma
suma(4,0) == 4

from paquete import *
suma(10,15) == 25
