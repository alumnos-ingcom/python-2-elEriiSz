################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Obtener el n-esimo termino de la sucecion de fibonacci
"""

def fibonacci_n(n):
    """Hace la secuencia de fibonacci hasta que se repitio la cantidad
    de veces que el usuario establecion"""
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
    numero = int(input("Ingrese la posicion del numero de fibonacci que quiere ver: "))
    resultado = fibonacci_n(numero)
    print(resultado)


if __name__ == "__main__":
    principal()
