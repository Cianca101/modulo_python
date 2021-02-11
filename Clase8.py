### Ejercicio Crear las siguientes funciones

# Crear un diccionario

# Función para registrar usuario en dict (data)
    #nombre, edad, ciudad de residencia
# Cada que se inserta usuario, asignarle un ID que contendra
    # ID = nombre, edad, ciudad de residencia
# Validar que no exista en el diccionario
user_name = "Cianca"
user_age = 29
user_city = "Leon"

data_user = {}
id_user = 0

def user_create(user_name, user_age, user_city):
    global id_user
    data_user[id_user] = {"Name": user_name, "Age": user_age, "City": user_city}
    id_user += 1
    print(data_user)



#