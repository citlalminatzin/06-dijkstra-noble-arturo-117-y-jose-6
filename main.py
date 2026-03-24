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

def ejercicio_3a():
    """
    Regresa las distancias mínimas de todos
    los vértices entre sí
    """
    n = 8
    M1 = zeros((n,n))

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
    
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    n = 4
    M2 = zeros((n,n))

    M2[0,1] = 9
    M2[3,2] = 2
    M2[0,3] = 6
    M2[1,3] = 1
    M2[2,1] = 3

    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias
    
def ejercicio_3c():
    n = 4
    M3 = zeros((n,n))

    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6

    distancias = [dijkstra(M3, i) for i in range(n)]
    return distancias
    ...

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
