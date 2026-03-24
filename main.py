import networkx as nx
import matplotlib.pyplot as plt
from numpy import zeros
from math import inf

def create_adjacency_matrix() -> list[list[float]]:
    """
    Crea una matriz de adyacencia para el Ejercicio 4.
    Los nodos del 1 al 12 en el diagrama se mapearán a los índices del 0 al 11.
    """
    n = 12
    # Inicializamos con ceros usando numpy y lo convertimos a lista de listas
    M = zeros((n, n)).tolist()
    
    # Registramos los pesos de las aristas según las flechas de la Gráfica 4
    # Formato: M[origen][destino] = peso
    M[0][1] = 9.0   # 1 -> 2
    M[0][2] = 7.0   # 1 -> 3
    M[0][3] = 3.0   # 1 -> 4
    M[0][4] = 2.0   # 1 -> 5
    M[1][5] = 4.0   # 2 -> 6
    M[2][5] = 2.0   # 3 -> 6
    M[2][7] = 1.0   # 3 -> 8
    M[3][7] = 11.0  # 4 -> 8
    M[3][6] = 8.0   # 4 -> 7
    M[4][6] = 11.0  # 5 -> 7
    M[5][8] = 6.0   # 6 -> 9
    M[5][9] = 5.0   # 6 -> 10
    M[6][1] = 7.0   # 7 -> 2 (Note: the arrow clearly points from 7 to 2)
    M[6][7] = 2.0   # 7 -> 8
    M[6][9] = 3.0   # 7 -> 10
    M[7][9] = 4.0   # 8 -> 10
    M[7][10] = 6.0  # 8 -> 11
    M[8][11] = 4.0  # 9 -> 12
    M[9][11] = 6.0  # 10 -> 12
    M[10][11] = 6.0 # 11 -> 12
    
    return M

def dijkstra(M: list[list[float]], origin: int) -> list[list[float]]:
    """
    M : Matriz de pesos de una gráfica
    origin: índice del nodo inicial

    returns: 
    lista con las distancia de las rutas (D) y el origen de la arista 
    con la que terminó la ruta (P)
    """
    n = len(M)
    
    # ---
    # Paso 1: Inicializa las distancias
    # ---
    D = [inf] * n          # D[v] guarda el costo del camino mínimo
    D[origin] = 0.0
    
    P = [-1.0] * n         # P[v] guarda el nodo predecesor. Usamos -1 para "ninguno".
    permanentes = [False] * n  # ED: Conjunto de vértices ya evaluados
    
    # Iteramos para encontrar el camino más corto a todos los nodos
    for _ in range(n):
        # ---
        # Paso 5 / 2: Marcar y Actualizar el nodo permanente
        # ---
        # Encontramos el nodo 'u' no marcado con la menor distancia en D
        min_dist = inf
        u = -1
        for i in range(n):
            if not permanentes[i] and D[i] < min_dist:
                min_dist = D[i]
                u = i
                
        # Si u sigue siendo -1, significa que los nodos restantes son inalcanzables
        if u == -1:
            break
            
        permanentes[u] = True
        
        # ---
        # Paso 3: Identifica los nodos vecinos disponibles
        # ---
        for v in range(n):
            # Tu práctica indica que el 0 representa que no existe arista.
            # Comprobamos que haya conexión (M[u][v] > 0) y que el vecino no sea permanente
            if M[u][v] > 0 and not permanentes[v]:
                
                # ---
                # Paso 4: Reetiquetado
                # ---
                distancia_tentativa = D[u] + M[u][v]
                
                # Si la nueva ruta es mejor, actualizamos el vector D y registramos al predecesor
                if distancia_tentativa < D[v]:
                    D[v] = distancia_tentativa
                    P[v] = float(u)
                    
    # Retorna una lista con ambas sub-listas solicitadas en el Ejercicio 1
    return [D, P]

def minimal_distance(M: list[list[float]], origin: int, destination: int) -> float:
    """Devuelve la distancia mínima entre el orien y destinatino """
    # Ejecutamos Dijkstra desde el origen
    resultados = dijkstra(M, origin)
    
    # Extraemos el vector de distancias (D está en el índice 0)
    distancias = resultados[0]
    
    # Devolvemos la distancia específica al nodo destino
    return distancias[destination]

def camino_optimo(M: list[list[float]], origin: int, destination: int) -> list[int]:
    """
    Utiliza el algoritmo de Dijkstra para encontrar la secuencia de vértices
    que conforman el camino más corto entre un origen y un destino.
    """
    # Ejecutamos tu función Dijkstra
    resultados = dijkstra(M, origin)
    
    # Extraemos el vector de distancias (D) y el de predecesores (P)
    D = resultados[0]
    P = resultados[1]
    
    # Si la distancia al destino es infinito, significa que es inalcanzable
    if D[destination] == inf:
        return [] # Retornamos una lista vacía indicando que no hay ruta
        
    ruta = []
    nodo_actual = destination
    
    # Rastrear hacia atrás usando el arreglo de predecesores P
    while nodo_actual != -1:
        ruta.append(int(nodo_actual))
        
        # Si llegamos al origen, terminamos de rastrear
        if nodo_actual == origin:
            break
            
        # Nos movemos al nodo que nos trajo a este
        nodo_actual = P[int(nodo_actual)]
        
    # Como rastreamos del destino al origen, invertimos la lista
    ruta.reverse()
    
    return ruta

#------------------ EJERCICIO 1

def ejercicio_1():
    """
    Regresa las distancias mínimas del
    primer vértice a todos los demás
    """
    n = 4
    MD = zeros((n, n))
    MD[0,1] = 9
    MD[3,2] = 2
    MD[0,3] = 6
    MD[1,3] = 1
    MD[2,1] = 3
    
    return dijkstra(MD, 0)

#------------------- EJERCICIO 2

def prueba_ejercicio_2():
    n = 4
    MD = zeros((n, n))
    MD[0,1] = 9
    MD[3,2] = 2
    MD[0,3] = 6
    MD[1,3] = 1
    MD[2,1] = 3
    
    origen = 0
    destino = 2
    
    distancia = dijkstra(MD, origen)[0][destino]
    ruta = camino_optimo(MD, origen, destino)
    
    print(f"Distancia mínima de {origen} a {destino}: {distancia}")
    print(f"Camino óptimo: {ruta}")

#------------------ EJERCICIO 3

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def analizar_grafica(M, origen, es_dirigida, titulo):
    """
    Usa las funciones dijkstra y camino_optimo para calcular el camino más corto y utiliza 
    NetworkX para estructurar y dibujar la gráfica.
    """
    print(f"\n{'-'*15} {titulo} {'-'*15}")
    
    # 1. Convertimos la matriz numpy a lista de listas para compatibilidad con tus funciones
    M_lista = M.tolist()
    
    # 2. Calculamos los resultados con tu algoritmo de Dijkstra
    distancias, predecesores = dijkstra(M_lista, origen)
    
    print(f"Resultados desde el nodo origen {origen}:")
    for destino in range(len(M_lista)):
        if distancias[destino] != float('inf'):
            ruta = camino_optimo(M_lista, origen, destino)
            print(f"  A nodo {destino} -> Distancia: {distancias[destino]} | Ruta: {ruta}")
        else:
            print(f"  A nodo {destino} -> Inalcanzable")
            
    # 3. Construimos el objeto NetworkX
    # nx.from_numpy_array detecta automáticamente los pesos y descarta los ceros
    if es_dirigida:
        G = nx.from_numpy_array(M, create_using=nx.DiGraph)
    else:
        G = nx.from_numpy_array(M, create_using=nx.Graph)
        
    # 4. Dibujamos la gráfica
    plt.figure(figsize=(7, 5))
    plt.title(f"{titulo} - Camino más corto desde nodo {origen}")
    
    # spring_layout organiza los nodos de forma atractiva
    pos = nx.spring_layout(G, seed=42) 
    
    # Dibujamos los nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='#A0CBE2', 
            node_size=600, font_weight='bold', font_color='black', 
            edge_color='gray', arrows=es_dirigida)
    
    # Añadimos las etiquetas de peso a las aristas
    pesos = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_color='red')
    
    plt.show()

# --- DEFINICIÓN DE LAS MATRICES ---

# Gráfica 1 (No dirigida, 8x8) [cite: 103, 107]
M1 = np.zeros((8, 8))
M1[0,1] = M1[1,0] = 3
M1[1,2] = M1[2,1] = 1
M1[0,3] = M1[3,0] = 2
M1[3,2] = M1[2,3] = 3
M1[1,4] = M1[4,1] = 4
M1[2,5] = M1[5,2] = 2
M1[2,6] = M1[6,2] = 2
M1[3,6] = M1[6,3] = 4
M1[4,7] = M1[7,4] = 6
M1[5,7] = M1[7,5] = 4
M1[5,6] = M1[6,5] = 3
M1[6,7] = M1[7,6] = 5

# Gráfica 2 (Dirigida, 4x4) [cite: 122, 127]
M2 = np.zeros((4, 4))
M2[0,1] = 9
M2[3,2] = 2
M2[0,3] = 6
M2[1,3] = 1
M2[2,1] = 3

# Gráfica 3 (Dirigida, 4x4) [cite: 135, 139]
M3 = np.zeros((4, 4))
M3[0,1] = 4
M3[0,2] = 8
M3[0,3] = 16
M3[1,2] = 5
M3[1,3] = 11
M3[2,3] = 6

# --- EJECUCIÓN ---
analizar_grafica(M1, origen=0, es_dirigida=False, titulo="Gráfica 1")
analizar_grafica(M2, origen=0, es_dirigida=True,  titulo="Gráfica 2")
analizar_grafica(M3, origen=0, es_dirigida=True,  titulo="Gráfica 3")

#------------------ EJERCICIO 4

def create_adjacency_matrix() -> list[list[float]]:
    """
    Crea la matriz de adyacencia para la gráfica 4 basada en los datos de distances.csv. 
    Se resta 1 a cada nodo para ajustar al indexado.
    """
    n = 12
    # Inicializamos la matriz de costos MD con ceros [cite: 63, 73]
    M = zeros((n, n)).tolist()
    
    # Datos proporcionados: origin, destination, weight
    aristas = [
        (1,2,9), (1,3,7), (1,4,3), (1,5,2), (2,6,4), (2,7,2), (2,8,1),
        (3,6,2), (3,7,7), (4,8,11), (5,7,11), (5,8,8), (6,9,6), (6,10,5),
        (7,9,4), (7,10,3), (8,10,5), (8,11,6), (9,12,4), (10,12,6), (11,6,12)
    ]
    
    for u, v, w in aristas:
        # Ajuste de nodo 1-12 a índice 0-11
        M[u-1][v-1] = float(w)
        
    return M

def ejercicio_4():
    """
  Encuentra la distancia mínima desde el nodo 1 hacia todos los demás y organiza el diagrama para 0-11
    """
    matriz = create_adjacency_matrix()
    # Ejecutamos Dijkstra partiendo del nodo 1 (índice 0) [cite: 101]
    resultados = dijkstra(matriz, 0)
    
    distancias = resultados[0]
    predecesores = resultados[1]
    
    print("Resultados Ejercicio 4 (Desde Nodo 1):")
    for i in range(len(distancias)):
        print(f"Al Nodo {i+1}: Distancia = {distancias[i]}, Predecesor = {int(predecesores[i])+1 if predecesores[i] != -1 else 'N/A'}")
    
    return resultados

if __name__ == "__main__":
    main()
