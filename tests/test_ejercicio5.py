################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.practica.ejercicio5 import corchetes_balanceados


def test_balanceados_true():
    cadena = "{[()]}"
    resultado = corchetes_balanceados(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == True, "el resultado debe ser True"

def test_balanceados_false():
    cadena = "{[[()]{"
    resultado = corchetes_balanceados(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == False, "el resultado debe ser False"


