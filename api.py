from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Definimos la clase Nodo
class Nodo:
    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre
        self.hijos = []

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_hijos(self, *hijos):
        self.hijos.extend(hijos)

    def get_hijos(self):
        return self.hijos


# Definimos la API
app = FastAPI()

# Modelo para recibir la solicitud
class BusquedaRequest(BaseModel):
    estado_inicial: List[int]
    estado_objetivo: List[int]


# Función de búsqueda DFS
def buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())

    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial 
    
    # Crear los hijos del nodo actual
    dato_nodo = nodo_inicial.get_datos()
    hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]], nodo_inicial)
    hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]], nodo_inicial)
    hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]], nodo_inicial)

    nodo_inicial.set_hijos(hijo_izquierdo, hijo_central, hijo_derecho)

    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados)
            if sol is not None:
                return sol

    return None


@app.post("/buscar")
async def buscar_solucion(request: BusquedaRequest):
    estado_inicial = request.estado_inicial
    estado_objetivo = request.estado_objetivo
    visitados = []

    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = buscar_solucion_DFS_rec(nodo_inicial, estado_objetivo, visitados)

    # Construir el resultado
    resultado = []
    if nodo_solucion:
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        return {"camino": resultado}
    
    return {"mensaje": "No se encontró solución"}

##