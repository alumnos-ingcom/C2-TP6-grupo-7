################
# Martín Carosanti - Hernan Palumbo
#Anagrama
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""Implementar una funcion que determine si dos cadenas son anagramas entre si, ignorando espacios
y diferencias entre mayusculas y minusculas. (En el repositorio hay un archivo con ejemplos)"""

def estandarizar_palabras(palabra):
    replace = {'á': 'a', 'é':'e', 'í':'i', 'ó':'o', 'ú': 'u', ' ': '', ',' : '', '.': ''}
    palabra.lower
    for caracter in replace.keys():
        palabra = palabra.lower().strip().replace(caracter, replace[caracter])
    return palabra

def separador_palabras(linea, separador= '–'):
    palabras = linea.split(separador, 1)
    return palabras

def anagrama(palabra1, palabra2):
    """Convertimos primero ambas listas a minúsculas, ignorando espacios y acentos"""
    palabra1 = estandarizar_palabras(palabra1)
    palabra2 = estandarizar_palabras(palabra2)
   
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

def buscar_anagramas_archivo(ruta_archivo):
    with open(ruta_archivo, encoding='utf-8') as f:
        anagramas = []
        for linea in f.readlines():
            palabras = separador_palabras(linea)
            palabras_a_estandarizar = palabras.copy()
            for palabra in palabras_a_estandarizar:
                palabras_a_estandarizar[palabras_a_estandarizar.index(palabra)] = estandarizar_palabras(palabra)
            if len(palabras)>1:
                es_anagrama = anagrama(palabras_a_estandarizar[0], palabras_a_estandarizar[1])
                palabras.append(es_anagrama)
                anagramas.append(palabras)
    return anagramas

def principal():
    """Toda la interacción con el usuario va acá"""
    for anagrama_analizado in buscar_anagramas_archivo('./anagramas.txt'):
        print(f'las palabras {anagrama_analizado[0]} y {anagrama_analizado[1]}', 'son angramas' if anagrama_analizado[-1] else 'NO son Anagramas')

if __name__ == "__main__":
    principal()