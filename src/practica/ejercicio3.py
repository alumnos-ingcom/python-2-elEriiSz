################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Obtener el grado de superposicion de una lista con la otra
"""
# Reemplazar por las funciones del ejercicio

def superpuestos(cadena, cadena_v):
    cont = 0
    if cadena_v[0] in cadena:
        for i in range(cadena.index(cadena_v[0]),(len(cadena_v))):
            if cadena[i]==cadena_v[i]:
                cont = cont +1
    posicion = cadena.index(cadena_v[0])
    return posicion, cont
    
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    cadena_v = ['H', 'o', 'l', 'a']
    posicion, cont = superpuestos(cadena, cadena_v)
    print(f"Grado de superposicion: {cont}")
    print(f"Desde {posicion} hasta {cont-1} de la lista {cadena}")            


if __name__ == "__main__":
    principal()
