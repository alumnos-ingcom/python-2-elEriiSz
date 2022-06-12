################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Obtener el n-esimo termino de la sucecion de fibonacci
"""
# Reemplazar por las funciones del ejercicio

def fibonacci_n(n):
    a = 0
    b = 1
    sum = 0
    count = 1
    while(count <= n):
        count += 1
        a = b
        b = sum
        sum = a + b
    return sum

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese la posicion del numero de fibonacci que quiere ver: "))
    resultado = fibonacci_n(numero)
    print(resultado)


if __name__ == "__main__":
    principal()
