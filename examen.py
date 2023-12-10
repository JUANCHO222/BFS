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
        'EDO.MEX':{'QRO':390, 'SLP':599, 'SONORA':1113},
        'PUEBLA':{'HIDALGO':395, 'SLP':437},
        'CDMX':{'MICHOACAN':346},
        'MICHOACAN':{'SONORA':869},
        'SLP':{'QRO':203, 'PUEBLA':437, 'EDO.MEX':599, 'SONORA':514, 'GUADALAJARA':423},
        'QRO':{'EDO.MEX':390, 'SLP':203},
        'HIDALGO':{'PUEBLA':395, 'GUADALAJARA':800, 'SONORA':827},
        'GUADALAJARA':{'HIDALGO':800, 'SLP':423},
        'MONTERREY':{'SONORA':1027},
        'SONORA':{'MONTERREY':1027, 'HIDALGO':827, 'SLP':514, 'EDO.MEX':1113, 'MICHOACAN':869}
    }
    estado_inicial='EDO.MEX'
    solucion='HIDALGO'
    metrosC = str(16 * 2.50 * 2.60)
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
    peaje ={
        'EDO.MEX':{'QRO':390, 'SLP':599, 'SONORA':1113},
        'PUEBLA':{'HIDALGO':395, 'SLP':437},
        'CDMX':{'MICHOACAN':346},
        'MICHOACAN':{'SONORA':869},
        'SLP':{'QRO':203, 'PUEBLA':437, 'EDO.MEX':599, 'SONORA':514, 'GUADALAJARA':423},
        'QRO':{'EDO.MEX':390, 'SLP':203},
        'HIDALGO':{'PUEBLA':395, 'GUADALAJARA':800, 'SONORA':827},
        'GUADALAJARA':{'HIDALGO':800, 'SLP':423},
        'MONTERREY':{'SONORA':1027},
        'SONORA':{'MONTERREY':1027, 'HIDALGO':827, 'SLP':514, 'EDO.MEX':1113, 'MICHOACAN':869}
    }
    sumaH = 0
    for i in range(len(resultado)-1):
        sumaH += peaje[resultado[i]][resultado[i+1]]
    
    #if metrosC=='110.0 m3':
    #    print("Horas: " + str(nodo_solucion.get_coste()/110.0))
    #elif metrosC=='104.0 m3':
    #    print("Horas: " + str(nodo_solucion.get_coste()/104.0))
    #else:
    #    print("Horas: " + str(sumaH*.3))
    print("Volumetria: " + metrosC + ' m3')
    print("Horas: " + str(nodo_solucion.get_coste()/104.0))
    print()