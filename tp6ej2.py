################
# Martín Carosanti - Hernan Palumbo
# Anagrama II
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""Procesar el archivo de anagramas y verificar si todos los de la lista son anagramas. 
Solo es necesario indicar las palabras de cada linea son anagramas entre si.
Envien las palabras evaluadas y si son o no anagramas entre si por consola."""

def estandarizar_palabras(palabra):
    """Convertimos primero ambas palabras en las listas a minúsculas, ignorando espacios y acentos"""
    replace = {'á': 'a', 'é':'e', 'í':'i', 'ó':'o', 'ú': 'u', ' ': '', ',' : '', '.': ''}
    palabra.lower
    for caracter in replace.keys():
        palabra = palabra.lower().strip().replace(caracter, replace[caracter])
    return palabra

def separador_palabras(linea, separador= '–'):
    palabras = linea.split(separador, 1)
    return palabras

def anagrama(palabra1, palabra2):
    palabra1 = estandarizar_palabras(palabra1)
    palabra2 = estandarizar_palabras(palabra2)
   
    """convertimos las cadenas a arreglos y las ordenamos"""
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    
    """Convertimos de vuelta a cadena una vez ordenadas"""
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    """Comprobamos la igualdad de las palabras"""
    return palabra1_ordenada == palabra2_ordenada

def buscar_anagramas_archivo(ruta_archivo):
    with open(ruta_archivo, encoding='utf-8') as f:
        anagramas = []
        for linea in f.readlines():
            palabras = separador_palabras(linea)
            for palabra in palabras:
                palabras[palabras.index(palabra)] = estandarizar_palabras(palabra)
            if len(palabras)>1:
                es_anagrama = anagrama(palabras[0], palabras[1])
                palabras.append(es_anagrama)
                anagramas.append(palabras)
    return anagramas

def principal():
    """Toda la interacción con el usuario va acá"""
    for anagrama_analizado in buscar_anagramas_archivo('./anagramas.txt'):
        print(f'las palabras [{anagrama_analizado[0]}] y [{anagrama_analizado[1]}]', 'son angramas' if anagrama_analizado[-1] else 'NO son Anagramas')

if __name__ == "__main__":
    principal()
