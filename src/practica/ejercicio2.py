################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#Precondiciones: Que la entrada sea una lista de numeros enteros
###############################################################
#Poscondiciones: Que la salida devuelva un tuple
"""
Devuelve un tuple con el maximo, minimo y promedio de una secuencia de numeros
"""

def estadisticas(lista):
    """Se ordena la secuencia de mayor a menor para despues indentificar
    facilmente el mayor y el menor. Despues se reccorre la nueva lista
    para sumar la secuencia y asi sacar el promedio. Luego se devuelve
    una tupla con la primera posicion siendo el mayor, la segunda el 
    menor y la tercera el promedio"""
    i = 0
    promedio = 0
    while i <= len(lista):
        j = 1
        while j <= len(lista)-1:
            if lista[j-1]<lista[j]:
                almacen = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = almacen
            j = j+1
        i=i+1
    i = 1 
    while i <= len(lista):
        promedio=promedio+lista[i-1]
        i=i+1
    promedio = promedio/len(lista)
    lista_retorno = [lista[0],lista[-1],promedio]
    return tuple(lista_retorno)

def principal():
    """
    Se ingresa una secuencia de numeros hasta que el usurio ingresa una
    letra. Al ingresarse una letra, la lista de la secuencia de numeros
    es 'enviada' a la funcion.
    """
    lista = []
    entrada = 0
    while entrada != "salir":
        entrada = input("Ingrese un numero para agregar (si desea terminar, ingrese una letra): ")
        try:
            entrada = int(entrada)
            lista.append(entrada)
        except ValueError as exc:
            entrada = "salir"

    maximo, minimo, promedio = estadisticas(lista)
    print(f"El maximo es {maximo}\nEl minimo es {minimo}\ny el promedio es {promedio}")

if __name__ == "__main__":
    principal()
