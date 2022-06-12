################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.practica.ejercicio1 import es_par


def test_es_par():
    numero = 10
    resultado =es_par(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == True, "el resultado para el valor 10, debe ser True"


def test_no_es_par():
    numero = 5
    resultado =es_par(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == False, "el resultado para el valor 5, debe ser False"


def test_negativo_par():
    numero = -10
    resultado =es_par(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == True, "el resultado para el valor -10, debe ser True"


def test_negativo_impar():
    numero = -5
    resultado =es_par(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == False, "el resultado para el valor -5, debe ser False"
