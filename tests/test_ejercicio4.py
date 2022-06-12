################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio4.py` que esta en
`src/practica`
"""

import pytest

from src.practica.ejercicio4 import fibonacci_n


def test_fibonacci_n():
    n = 5
    resultado = fibonacci_n(n)
    assert isinstance(resultado, int), "el resultado debe ser un entero"
    assert resultado == 5, "el resultado debe ser 5"

def test_fibonacci_n_negativo():
    n = -5
    resultado = fibonacci_n(n)
    assert isinstance(resultado, int), "el resultado debe ser un entero"
    assert resultado == 0, "el resultado debe ser 0"


