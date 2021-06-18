################
# Martín Carosanti - Hernan Palumbo
#Copiadora
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import shutil

class ErrorArchivo(Exception):
    pass

def copiadora(archivo_entrada, archivo_salida):
    try:
        shutil.copy(archivo_entrada, archivo_salida)
    except FileNotFoundError as err:
        raise ErrorArchivo('El archivo de entrada no existe vuelva a intentar') from err

def principal():
    """Toda la interacción con el usuario va acá"""
    try:
        archivo_entrada = input('ingrese ruta de archivo a copiar: ')
        archivo_salida = input('ingrese ruta de archivo de salida: ')
        copiadora(archivo_entrada, archivo_salida)
    except ErrorArchivo as err:
        print (err)

if __name__ == "__main__":
    principal()