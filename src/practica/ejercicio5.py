################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Saber si los simbolos estan balanceados(si para cada simbolo abierto hay uno cerrado)
"""

def corchetes_balanceados(cadena):
    """
    Guarda en una nueva lista solamente los simbolos en orden de aparicion. Luego 
    verifica si esos simbolos coinciden con los de apertura y si luego tienen cierre
    al sumar 1 si hay una apertura y restar 1 si hay un simbolo cerrador. Si baja de 
    0, significa que hay un simbolo cerrador antes de que haya algun simbolo de apertura
    'disponible', por lo que directamente devuelve falso.
    """
    cadena_nueva = ""
    simbolos = "{[()]}"
    i = 0
    while i<len(cadena):
        if cadena[i] in simbolos:
            cadena_nueva = cadena_nueva + cadena[i]
        i = i +1
    i = 0
    cont = 0
    while i<len(cadena_nueva):
        if cadena_nueva[i] in simbolos[:3]:
            cont = cont + 1
        else:
            cont = cont - 1
        if cont<0:
            i = len(cadena_nueva)-1
        i = i +1
    return cont==0

def principal():
    cadena = input("Ingrese la cadena a verificar: ")
    resultado = corchetes_balanceados(cadena)
    print(f"Los simbolos de la cadena estan abiertos y cerrados correctamente? {resultado}")


if __name__ == "__main__":
    principal()
