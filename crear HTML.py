################
# Martín Carosanti - Hernan Palumbo
# Crear HTML
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def principal():
    """Toda la interacción con el usuario va acá"""
    pass

if __name__ == "__main__":
    principal()
    
import webbrowser
    pagina = open("prueba.html","w")
    contenido = ("Esto es un parrafo")
    """
    <html>
        <body>
            <h1>Hola HTML</h1>
        </body>
    </html>
    """
    pagina.write(contenido)
    pagina.close()