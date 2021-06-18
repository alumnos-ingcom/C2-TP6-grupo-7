################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class CaracterIncorrecto(Exception):
    pass

def rotador_indices(lista,indice_inicial,numero_rotaciones, sentido_inverso=False):
    """ dada una lista y el indice inicial dentro de la lista devuelve el indice que le
    corresponde despues de rotarlo una cierta cantidad de veces"""
    
    if sentido_inverso == False:
        lista_nueva = lista.copy()
        while (indice_inicial + numero_rotaciones) > (len(lista_nueva) - 1):
            lista_nueva.extend(lista)
        return lista.index(lista_nueva[indice_inicial + numero_rotaciones])
    
    if sentido_inverso == True:
        lista_nueva = lista.copy()
        lista_nueva = list(reversed(lista_nueva))
        nuevo_indice = ((len(lista)-1) - indice_inicial)
        while nuevo_indice + numero_rotaciones > (len(lista_nueva)-1):
            lista_nueva.extend(list(reversed(lista)))
        return lista.index(lista_nueva[nuevo_indice + numero_rotaciones])

def rot_n(caracter,numero_rotaciones, sentido_inverso = False):
    """solo se admiten caracteres [0-9][A-Z][a-z]
    la funcion toma el caracter y lo rota una cantidad de veces igual a numero_rotaciones """
    
    lista_a_z = list(range(ord('a'), ord('z')+1))
    lista_A_Z = list(range(ord('A'), ord('Z')+1))
    lista_0_9 = list(range(ord('0'), ord('9')+1))
    ord_caracter = ord(caracter)

    if ord_caracter in lista_a_z:
        index = lista_a_z.index(ord_caracter)
        nuevo_indice = rotador_indices(lista_a_z, index, numero_rotaciones, sentido_inverso)
        caracter_rotado = chr(lista_a_z[nuevo_indice])
    elif ord_caracter in lista_A_Z:
        index = lista_A_Z.index(ord_caracter)
        nuevo_indice = rotador_indices(lista_A_Z, index, numero_rotaciones, sentido_inverso)
        caracter_rotado = chr(lista_A_Z[nuevo_indice]) 
    elif ord_caracter in lista_0_9:
        index = lista_0_9.index(ord_caracter)
        nuevo_indice = rotador_indices(lista_0_9, index, numero_rotaciones, sentido_inverso)
        caracter_rotado = chr(lista_0_9[nuevo_indice])
    else:
        caracter_rotado = caracter
    return caracter_rotado

def cifrador(mensaje, rotaciones):
    """dado el mensaje realiza el cifrado por rotaciones utilizando 
    la cantidad de rotaciones dadas en la variable rotaciones los caracteres permitdos en mensaje son:
    [a-z][A-Z][0-9]"""

    lista_mensaje = []
    lista_mensaje[:0] = mensaje
    for i in range(len(lista_mensaje)):
        lista_mensaje[i] = rot_n(lista_mensaje[i], rotaciones)
    return ''.join(lista_mensaje)

def decifrador(mensaje, rotaciones):
    """dado el mensaje realiza el decifrado de un mensaje por rotaciones utilizando
    la cantidad de rotaciones dadas en la variable rotaciones los caracteres permitdos en mensaje son:
    [a-z][A-Z][0-9]"""
    lista_mensaje = []
    lista_mensaje[:0] = mensaje
    for i in range(len(lista_mensaje)):
        lista_mensaje[i] = rot_n(lista_mensaje[i], rotaciones, sentido_inverso=True)
    return ''.join(lista_mensaje)


def prueba():
    try:
        """Toda la interacción con el usuario va acá"""
        mensaje = 'hola030645645'
        mensaje_cifrado = cifrador(mensaje, 13)
        mensaje_descifrado = decifrador(mensaje_cifrado,13)
        print(mensaje_descifrado)
    except CaracterIncorrecto as e:
        print(e)
    
if __name__ == "__main__":
    prueba()

