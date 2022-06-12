################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.practica.ejercicio6 import encriptar_por_n, desencriptar_por_n


def test_encriptacion_true():
    cadena = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    n = 13
    resultado = encriptar_por_n(cadena, n)
    assert isinstance(resultado, str), "el resultado debe ser un str"
    assert resultado == "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm", "el resultado deberia ser nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm "

def test_desencriptacion_true():
    cadena = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    n = 13
    resultado = encriptar_por_n(cadena, n)
    assert isinstance(resultado, str), "el resultado debe ser un str"
    assert resultado == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "El resultado deberia ser ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

