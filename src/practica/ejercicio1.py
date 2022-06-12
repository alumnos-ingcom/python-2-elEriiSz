################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#Precondiciones: Que la entrada sea un entero
###############################################################
#Poscondiciones: Que la salida devuelva un bool
"""
Devuelve True si el numero ingresado es par y False si es impar
"""

def es_par(num):
    """Se comprueba que el numero detras de la coma sea un 0"""
    return str(num/2)[-1]=="0"

def principal():
    numero = int(input("Ingrese numero entero a comprobar: "))
    resultado = es_par(numero)
    print(resultado)

if __name__ == "__main__":
    principal()
