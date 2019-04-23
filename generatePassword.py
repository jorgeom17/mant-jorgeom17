import string
import random

#Funcion que genera contraseñas de forma aleatoria entre 4 y 16 caracteres
def generatePassword():


    clave = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    longitud = random.randint(4, 16)
    
    return ''.join(random.choice(clave) for i in range(longitud))
