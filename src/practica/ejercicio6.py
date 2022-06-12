################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Encriptar y/o desencriptar una cadena con el cifrado cesar con un numero n
"""

def encriptar_por_n(cadena, n):
    """
    Encripta una cadena dada al sumar o restar n a su caracter unicode
    """
    cadena_encr = ""
    for i in cadena:
        if ord(i) >64 and ord(i) <91:
            if ord(i)+n > 90:
                cadena_encr = cadena_encr + chr(ord(i)-26+n)
            else:
                cadena_encr = cadena_encr + chr(ord(i)+n)
        elif ord(i) >96 and ord(i) <123:
            if ord(i)+n > 122:
                cadena_encr = cadena_encr + chr(ord(i)-26+n)
            else:
                cadena_encr = cadena_encr + chr(ord(i)+n)
        else:
            cadena_encr = cadena_encr + i
    return cadena_encr


def desencriptar_por_n(cadena, n):
    """
    Desencripta una cadena dada al sumar o restar n a su caracter unicode
    """
    cadena_decr = ""
    for i in cadena:
        if ord(i) >64 and ord(i) <91:
            if ord(i)-n < 65:
                cadena_decr = cadena_decr + chr(ord(i)+26-n)
            else:
                cadena_decr = cadena_decr + chr(ord(i)-n)
        elif ord(i) >96 and ord(i) <123:
            if ord(i)-n < 97:
                cadena_decr = cadena_decr + chr(ord(i)+26-n)
            else:
                cadena_decr = cadena_decr + chr(ord(i)-n)
        else:
            cadena_decr = cadena_decr + i
    return cadena_decr


def principal():
    cadena = input("Ingrese la cadena a encriptar: ")
    n = int(input("Ingrese numero por el cual encriptar: "))
    encriptacion = encriptar_por_n(cadena, n)
    print(encriptacion)
    desencriptacion = desencriptar_por_n(encriptacion, n)
    print(desencriptacion)


if __name__ == "__main__":
    principal()
