def Floyda_Warshalla(matrix):
    n =len(matrix)
    distance = [[float("inf")]*n for i in range(n)]
    previous = [[None]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            elif matrix[i][j] != 0:
                distance[i][j] = matrix[i][j]
                previous[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    previous[i][j] = previous[k][j]
    return distance, previous

graph = [
    [0, 2, float('inf'), 1, float('inf')],
    [2, 0, 3, float('inf'),float('inf')],
    [float('inf'), 3, 0, 4, 2],
    [1, float('inf'), 4, 0, 5],
    [float('inf'), float('inf'), 2, 5, 0]
]

distance, previous = Floyda_Warshalla(graph)
print("Macierz najkrótszych odległości między węzłami: ")
for row in distance:
    print(row)
print("Macierz poprzedników: ")
for row in previous:
    print(row)


