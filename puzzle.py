# Puzzle lineal con busqueda en amplitud
from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()  # Extraer el último nodo (LIFO), FIFO .pop(0)
        # Extraer al nodo y añadir a visitados
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # Solución encontrada
            solucionado = True
            return nodo
        else:
            # Expandir los nodos hijos
            dato_nodo = nodo.get_datos()

            # Operador Izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo, nodo)
            if not hijo_izquierdo.en_lista(nodos_visitados)\
                  and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)

            # Operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo,nodo)
            if not hijo_central.en_lista(nodos_visitados)\
                  and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            # Operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo, nodo)
            if not hijo_derecho.en_lista(nodos_visitados)\
                  and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)

    return None


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    if nodo_solucion:
        # Mostrar Resultado
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()  
        print(resultado)