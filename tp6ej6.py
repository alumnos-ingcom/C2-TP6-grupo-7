################
# Martín Carosanti - Hernan Palumbo
# Etiquetas HTML
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hace_etiqueta(contenido, etiqueta):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará <h1>Hola</h1>
    '''
    return '<%s>%s</%s>' % (etiqueta, contenido, etiqueta)

def hace_comenta(contenido):
    """
    Retorna el contenido envuelto en las marcas de comentario HTML
    <p><h1>Hola HTML</h1>Párrafo</p> (separen las marcas del contenido con un espacio)"""     
    contenido = (<!-- Esto es un parrafo  -->)
    pass

def principal():
    """Toda la interacción con el usuario va acá"""
    encabezado = hace_etiqueta('Hola HTML', 'h1')
    print(encabezado)
    parrafo = hace_etiqueta(encabezado+' Párrafo', 'p')
    print(parrafo)
    
    
if __name__ == "__main__":
    principal()