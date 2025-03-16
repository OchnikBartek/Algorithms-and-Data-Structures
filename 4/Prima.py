import sys
def Prim(matrix):
    selected = [False] * int(len(matrix))
    num_edges = 0
    total_weight = 0
    mst_edges = []
    selected[0] = True

    while num_edges < int(len(matrix)) - 1:
       minimum = sys.maxsize
       x = -1
       y = -1
       for i in range(len(matrix)):
           if selected[i]:
               for j in range(len(matrix)):
                   if not selected[j] and matrix[i][j]:
                       if matrix[i][j] < minimum:
                           minimum = matrix[i][j]
                           x = i
                           y = j
       if x == -1 and y == -1:
           print("Graf nie spójny")
           break
       mst_edges.append((x, y, matrix[x][y]))
       total_weight += matrix[x][y]
       selected[y] = True
       num_edges += 1

    mst_matrix = [[float('inf')] * len(matrix) for _ in range(len(matrix))]
    for edge in mst_edges:
        u, v, weight = edge
        mst_matrix[u][v] = float(weight)
        mst_matrix[v][u] = float(weight)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                mst_matrix[i][j] = 0.0


    return mst_edges, total_weight, mst_matrix

graph = [
    [0, 3, float('inf'), float('inf'), 3],
    [3, 0, 1, 3, float('inf')],
    [float('inf'), 1, 0, 3, float('inf')],
    [float('inf'), 3, 3, 0, float('inf')],
    [3, float('inf'), float('inf'), float('inf'), 0]
]
mst, total, matr = Prim(graph)
print("Krawędzie minimalnego drzewa rozpinającego:")
for edge in mst:
    print(f"Wierzchołek {edge[0]} - Wierzchołek {edge[1]} o wadze {edge[2]}")
for edge in matr:
    print(edge)
print(f"Łączna waga MST: {total}")
