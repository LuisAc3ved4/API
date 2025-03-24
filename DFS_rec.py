from arbol import Nodo

def buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())

    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial 
    
    # Crear los hijos del nodo actual
    dato_nodo = nodo_inicial.get_datos()
    hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
    hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
    hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])

    # Asignar el padre a los hijos
    hijo_izquierdo.set_padre(nodo_inicial)
    hijo_central.set_padre(nodo_inicial)
    hijo_derecho.set_padre(nodo_inicial)

    # Agregar los hijos al nodo inicial
    nodo_inicial.set_hijos(hijo_izquierdo, hijo_central, hijo_derecho)

    # Buscar en los hijos
    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:  
            sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados)   
            if sol is not None:
                return sol

    return None

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    visitados = []

    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados)

    # Mostrar el resultado
    resultado = []
    if nodo_solucion:
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
##