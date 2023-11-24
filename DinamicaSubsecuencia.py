#Funcion que calcula el largo maximo entre 2 elementos del array y retorna dicho elemento.
def maxdevuelvelist(lista, lista2):
    if lista[0] >= lista2[0]:
        return lista
    return lista2

#Input del programa.   
entrada = input("Por favor, ingresa una secuencia de números separados por espacios: ")
A = [int(num) for num in entrada.split()]

i = 1
j = len(A)

# Género la matriz de listas repleta de [0,0] añadiendo 1 columna y fila más para poder realizar comparaciones de subproblemas luego.
matriz = [[list([0, 0]) for _ in range(j + 1)] for _ in range(j + 1)]

# Asumo y calculo los subproblemas triviales de forma lineal. Calculo los largos y el valor de la suma interna de los problemas base.
for k in range(i, len(A) + 1):
    for p in range (0, len(A) + 1):
        if p==0:
            matriz[k][p][0] = 0
        elif k == p:
            matriz[k][p][0] = 1
        elif k == p - 1 or p == k - 1:
            matriz[k][p][0] = 2

#Declaro un mayor muy chico y mi respuesta final de indices.
mayor = -1
respuesta = ()

# Evito calcular nuevamente los problemas ya calculados usando ventanas a partir de tamaño 3 y extiendo la longitud 
# y actualizo el valor de su suma interna de la secuencia anterior si se cumple la condicion que se calcula
# basada en una memoizacion de los casos anteriores, tengo en cuenta tambien los casos de longitud 3 ya que
# estos son tratados de manera distinta debido a su longitud de suma interna igual a 0 (no tienen elementos entre medio).
for tamaño in range(3, j + 1): 
    for k in range(1, j - tamaño + 2):
        p = k + tamaño - 1
        if tamaño != 3:
            if matriz[k+1][p-1][1] + A[k] + A[p-2] <= A[k-1] and matriz[k+1][p-1][1] + A[k] + A[p-2] <= A[p-1]:
                matriz[k][p][0] = matriz[k+1][p-1][0] + 2
                matriz[k][p][1] = matriz[k+1][p-1][1] + A[k] + A[p-2]
            else:
                listamaxima = maxdevuelvelist(matriz[k][p-1], matriz[k+1][p])
                matriz[k][p][0] = listamaxima[0]
                matriz[k][p][1] = listamaxima[1]
        else:
            if A[k] <= A[k-1] and A[k] <= A[p-1]:
                matriz[k][p][0] = matriz[k+1][p-1][0] + 2
                matriz[k][p][1] = A[k]
            else:
                listamaxima = maxdevuelvelist(matriz[k][p-1], matriz[k+1][p])
                matriz[k][p][0] = listamaxima[0]
                matriz[k][p][1] = listamaxima[1]
        if matriz[k][p][0] > mayor:
            mayor = matriz[k][p][0]
            if mayor > 2:
                respuesta = (k-1, p-1)
            else:
                respuesta = (k-1, p-2)

#Output del problema.
print(f"Los índices que marcan los extremos de la subsecuencia más larga que cumple con las condiciones son: {respuesta}")