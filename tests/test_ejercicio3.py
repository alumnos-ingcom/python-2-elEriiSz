################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.practica.ejercicio3 import superpuestos


def test_superpuestos():
    cadena = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    cadena_v = ['H', 'o', 'l', 'a']
    posicion, cont = superpuestos(cadena, cadena_v)
    assert isinstance(posicion, int), "el resultado debe ser un entero"
    assert isinstance(cont, int), "el resultado debe ser un entero"
    assert posicion == 0, "el resultado debe ser 0"
    assert cont == 4, "el resultado debe ser 4"


