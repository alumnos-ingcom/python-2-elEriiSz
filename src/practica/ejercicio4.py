################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from math import sqrt
"""
Obtener el n-esimo termino de la sucecion de fibonacci
"""
# Reemplazar por las funciones del ejercicio

def fibonacci_n(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

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
