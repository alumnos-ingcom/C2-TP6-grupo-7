################
# Martín Carosanti - Hernan Palumbo
#Anagrama
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""Implementar una funcion que determine si dos cadenas son anagramas entre si, ignorando espacios
y diferencias entre mayusculas y minusculas. (En el repositorio hay un archivo con ejemplos)"""

def anagrama(palabra1, palabra2):
    """Convertimos primero ambas listas a minúsculas, ignorando espacios y acentos"""
    palabra1 = palabra1.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    palabra2 = palabra2.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    """convertimos las cadenas a arreglos y las ordenamos"""
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    """Convertimos de vuelta a cadena ua vez ordenadas"""
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    """Comprobamos la igualdas de las palabras"""
    return palabra1_ordenada == palabra2_ordenada

def principal():
    """Toda la interacción con el usuario va acá"""
    cadena1 = input("Ingresa una cadena: ")
    cadena2 = input("Ingresa otra cadena: ")
    es_anagrama = anagrama(cadena1, cadena2)
    if es_anagrama:
        print(f"La palabra: {cadena1} es anagrama de: ")
        print(f"{cadena2}")
    else:
        print(f"Las palabras: {cadena1} NO es anagrama de {cadena2}")

if __name__ == "__main__":
    principal()