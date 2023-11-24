# Descarta las aristas que estén conformadas por vertices ya saturados/ocupados
def descartarAristas(a, b, grafo):
    nuevo_grafo = []
    for tupla in grafo:
        if tupla[0] != a and tupla[0] != b and tupla[2] != a and tupla[2] != b:
            nuevo_grafo.append(tupla)
    return nuevo_grafo

# Input del programa
Grafo = [("q",57,"A"),("q",87,"B"),("q",75,"D"),("r",96,"C"),("r",55,"E"),("r",85,"F"),("s",48,"A"),("s",74,"C"),("s",64,"G"),("t",70,"B"),("t",81,"D"),("u",60,"C"),("u",26,"F"),("v",95,"A"),("v",60,"F"),("w",90,"D"),("w",75,"E"),("w",88,"G")]

# Declaracion del conjunto de arcos con mayor peso total
Matching = []

# Declaración del arreglo del que elegiremos las aristas para el matching
AristasDisponibles = Grafo

# Mientras haya aristas para añadir al matching:
while len(AristasDisponibles) != 0:
    mayor = None
    # Recorremos todas las aristas buscando la de mayor peso
    for tupla in AristasDisponibles:
        if mayor is None or tupla[1] > mayor[1]:
            mayor = tupla
    # Tras recorrer todo el array añadimos la arista de mayor peso al matching
    Matching.append(mayor)
    # Descartamos las aristas que tengan uno de sus vértices ya ocupados por el último agregado al matching
    AristasDisponibles = descartarAristas(mayor[0], mayor[2], AristasDisponibles)

print(Matching)