################
# Martín Carosanti - Hernan Palumbo
# Etiquetas HTML
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hace_etiqueta(contenido, etiqueta, salto=False):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará <h1>Hola</h1>
    '''
    if salto:
        salto = '\n'
    else:
        salto = ''

    return f'<%s>{salto}%s{salto}</%s>' % (etiqueta, contenido, etiqueta)

def hace_comenta(contenido):
    """
    Retorna el contenido envuelto en las marcas de comentario HTML
    <p><h1>Hola HTML</h1>Párrafo</p> (separen las marcas del contenido con un espacio)""" 
    
    return f'<!-- {contenido}  -->'

def principal():
    """Toda la interacción con el usuario va acá"""
    nombre_archivo = input('Ingrese el nombre del archivo html que quiere crear: ')

    with open(nombre_archivo + '.html', mode = 'a', encoding='utf-8') as f:
        encabezado = hace_etiqueta('Hola HTML', 'h1')
        parrafo = hace_etiqueta('Esto es un parrafo', 'p')
        body = hace_etiqueta(encabezado + '\n' + parrafo, 'body', salto=True)
        comentario = hace_comenta('Este es un comentario')
        html = hace_etiqueta(comentario + '\n' + body, 'html', salto=True )
        f.write(html)

if __name__ == "__main__":
    principal()