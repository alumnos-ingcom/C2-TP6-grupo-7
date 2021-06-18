################
# Martín Carosanti - Hernan Palumbo
#Codificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from cesar import cifrador
from tp6ej3 import ErrorArchivo
import re

def cifrador_archivo(ruta_archivo, rotaciones):
    try:
        with open(ruta_archivo, mode = 'r', encoding = 'utf-8') as f:
            lista_nombre_archivo = ruta_archivo.split('.')
            ruta_archivo_cifrado = lista_nombre_archivo[0] + '.cesar.'
            with open(ruta_archivo_cifrado, mode = 'w', encoding='utf-8') as f2:
                for linea in f.readlines():
                    palabras_a_cifrar = linea.split()
                    palabras_cifradas = []
                    for palabra in palabras_a_cifrar:
                        palabras_cifradas.append(cifrador(palabra, rotaciones))
                new_line = ' '.join(palabras_cifradas)
                f2.write(new_line)
    except FileNotFoundError:
        raise ErrorArchivo('No existe el archivo que desea cifrar')

def principal():
    try:
        """Toda la interacción con el usuario va acá"""
        cifrador_archivo('texto.txt', 13)
    except ErrorArchivo as err:
        print(err)

if __name__ == "__main__":
    principal()