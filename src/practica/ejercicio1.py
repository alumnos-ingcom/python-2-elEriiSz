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
    """Se utiliza la formula F-32/1.8 donde F son los grados fahrenheit"""
    return str(num/2)[-1]=="0"

def principal():
    """
    Se ingresan y convierten los grados celsius y fahrenheit
    """
    numero = int(input("Ingrese numero entero a comprobar: "))
    resultado = es_par(numero)
    print(resultado)

if __name__ == "__main__":
    principal()
