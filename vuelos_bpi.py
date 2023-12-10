# Vuelos con busqueda con profundidad iterativa
from arbol import Nodo

def DFS_prof_iter(nodo, solucion):
    for limite in range(0, 100): # Limitar la profundidad temporal
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol != None:
            return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir nodos hijo (Ciudades con Conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
        
            nodo.set_hijos(lista_hijos)
        
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    # Llamada Recursiva
                    sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1)
                    if sol != None:
                        return sol
    return None

if __name__ == '__main__':
    conexiones = {
            'EDO.MEX':{'QRO', 'SLP', 'SONORA'},
            'PUEBLA':{'HIDALGO', 'SLP'},
            'CDMX':{'MICHOACAN'},
            'MICHOACAN':{'SONORA'},
            'SLP':{'QRO', 'PUEBLA', 'EDO.MEX', 'SONORA', 'GUADALAJARA'},
            'QRO':{'EDO.MEX', 'SLP'},
            'HIDALGO':{'PUEBLA', 'GUADALAJARA', 'SONORA'},
            'GUADALAJARA':{'HIDALGO', 'SLP'},
            'MONTERREY':{'SONORA'},
            'SONORA':{'MONTERREY', 'HIDALGO', 'SLP', 'EDO.MEX', 'MICHOACAN'}
        }

    estado_inicial = 'EDO.MEX'
    solucion = 'HIDALGO'
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    # Mostrar Resultados
    if nodo != None:
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print('Solucion No encontrada')