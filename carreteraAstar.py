# Viaje por carretera con Búsqueda A*
import functools
from arbol import Nodo
from math import sin, cos, acos

def compara(x, y):
    # g(n) + h(n) para ciudad x
    lat1 = coord[x.get_datos()][0]
    lon1 = coord[x.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]

    d = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_coste() + d
    
    # g(n) + h(n) para ciudad y
    lat1 = coord[y.get_datos()][0]
    lon1 = coord[y.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]

    d = int(geodist(lat1, lon1, lat2, lon2))
    c2 = y.get_coste() + d
    return c1 - c2

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    rad_grad = 57.29577951
    longitud = lon1 - lon2
    val = (sin(lat1 * grad_rad) * sin(lat2 * grad_rad)) + (cos(lat1 * grad_rad) * cos(lat2 * grad_rad) * cos(longitud * grad_rad))
    return (acos(val) * rad_grad) * 111.32

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos Frontera
        nodos_frontera = sorted(nodos_frontera, key=functools.cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # Extraer nodo y añadirlo a nodos_visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion Encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                # Calculo g(n): Coste acumulado
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
            if not hijo.en_lista(nodos_visitados):
                # Si esta en lista lo sustituimos con el
                # nuevo valor de coste si es menor
                if hijo.en_lista(nodos_frontera):
                    for n in nodos_frontera:
                        if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)
                else:
                    nodos_frontera.append(hijo)
        nodo.set_hijos(lista_hijos)

if __name__ == '__main__':
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
    coord = {
        'Malaga':(36.43, -4.24),
        'Sevilla':(37.23, -5.59),
        'Granada':(37.11, -3.35),
        'Valencia':(39.28, -0.22),
        'Madrid':(40.24, -3.41),
        'Salamanca':(40.57, -5.40),
        'Santiago':(42.52, -8.33),
        'Santander':(43.28, -3.48),
        'Zaragoza':(41.39, -0.52),
        'Barcelona':(41.23, +2.11)
    }
    estado_inicial='EDO.MEX'
    solucion='HIDALGO'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    
    # Mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)
    print ('Coste: ' + str(nodo_solucion.get_coste()))