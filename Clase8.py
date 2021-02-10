### Ejercicio Crear las siguientes funciones

# Crear un diccionario

# Función para registrar usuario en dict (data)
    #nombre, edad, ciudad de residencia
# Cada que se inserta usuario, asignarle un ID que contendra
    # ID = nombre, edad, ciudad de residencia
# Validar que no exista en el diccionario

data_user = {}
user_name = "Cianca"
user_age = 29
user_city = "Leon"

id_user = f'{user_name}' + f'{user_age}' + f'{user_city}'

def user_create(user_name, user_age, user_city, id_user):
    id = f'{id_user}' + f'{1}'
    data_user[id] = {"Name": nombre, "Age": edad, "City": ciudad}


