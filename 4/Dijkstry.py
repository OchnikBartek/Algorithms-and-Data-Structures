def Dijkstry(matrix):
    selected = [False]*len(matrix)
    distance = [float('inf')]*len(matrix)
    distance[0] = 0
    previous = [None]*len(matrix)

    for i in range(len(matrix)):
        min_length = float('inf')
        x = -1
        for j in range(len(matrix)):
            if not selected[j] and distance[j] < min_length:
                min_length = distance[j]
                x = j
        if x == -1:
            print("Graf niespójny")
            break
        selected[x] = True

        for y in range(len(matrix)):
            if matrix[y][x] != 0 and not selected[y]:
                new_distance = distance[x] + matrix[x][y]
                if new_distance < distance[y]:
                    distance[y] = new_distance
                    previous[y] = x

    return distance, previous

graph = [
    [0, 3, float('inf'), float('inf'), 3],
    [3, 0, 1, 3, float('inf')],
    [float('inf'), 1, 0, 3, float('inf')],
    [float('inf'), 3, 3, 0, float('inf')],
    [3, float('inf'), float('inf'), float('inf'), 0]
]

dis_result, prev_result = Dijkstry(graph)

print("Najkrótsze odległości od wierzchołka startowego:", dis_result)
print("Poprzednicy na ścieżkach:", prev_result)

