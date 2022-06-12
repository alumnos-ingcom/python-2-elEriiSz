################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.practica.ejercicio2 import estadisticas


def test_estadisticas():
    lista = [1, 4, 10]
    resultado = estadisticas(lista)
    assert isinstance(resultado, tuple), "el resultado debe ser un tuple"
    assert resultado[0] == 10, "el resultado debe ser 10"
    assert resultado[1] == 1, "el resultado debe ser 1"
    assert resultado[2] == 5, "el resultado debe ser 5"

def test_estadisticas_negativa():
    lista = [-1, -4, -10]
    resultado = estadisticas(lista)
    assert isinstance(resultado, tuple), "el resultado debe ser un tuple"
    assert resultado[0] == -1, "el resultado debe ser -1"
    assert resultado[1] == -10, "el resultado debe ser -10"
    assert resultado[2] == -5, "el resultado debe ser -5"

