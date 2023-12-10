# Viaje por carretera con búsqueda de coste uniforme
import functools
from arbol import Nodo

def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0) #costo
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key= functools.cmp_to_key(compara))
        nodo=nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo sustituimos con
                    # el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste()>hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                    nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
    'EDO.MEX':{'SLP':513, 'CDMX':125},
    'CDMX':{'EDO.MEX': 125, 'MICHOACAN': 491, 'SLP': 423},
    'SLP':{'EDO.MEX': 513, 'CDMX': 423, 'MICHOACAN': 355, 'SONORA': 603, 'MONTERREY': 313, 'GUADALAJARA': 437, 'HIDALGO': 599, 'QRO': 203, 'PUEBLA': 514},
    'MICHOACAN':{'SONORA': 346, 'MONTERREY': 296},
    'QRO':{'HIDALGO': 390},
    'MONTERREY':{'SONORA': 296, 'QRO': 517},
    'GUADALAJARA':{},
    'SONORA':{},
    'HIDALGO':{},
    'PUEBLA':{}
    }
    estado_inicial='EDO.MEX'
    solucion='HIDALGO'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Distancia: " + str(nodo_solucion.get_coste()) +" km")
