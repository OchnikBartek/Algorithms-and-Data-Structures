def heuristic(node, goal):
    return abs(node - goal)


def a_star(matrix,start,goal):
    n = len(matrix)
    open_list = [start]
    came_from = {}
    g_score = {i: float('inf') for i in range(n)}
    g_score[start] = 0
    f_score = {i: float('inf') for i in range(n)}
    f_score[start] = heuristic(start, goal)
    while open_list:
        current = min(open_list, key=lambda x: f_score[x])
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        open_list.remove(current)
        for neighbor in range(n):
            if matrix[current][neighbor] != float('inf') and matrix[current][neighbor] > 0:
                tentative_g_score = g_score[current] + matrix[current][neighbor]
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None


graph = [
    [0, 2, float('inf'), 1, float('inf')],
    [2, 0, 3, float('inf'),float('inf')],
    [float('inf'), 3, 0, 4, 2],
    [1, float('inf'), 4, 0, 5],
    [float('inf'), float('inf'), 2, 5, 0]
]
Start = 0
Goal = 4
Path = a_star(graph,Start,Goal)
print(f"Znaleziono sciezke od elementu {Start} do {Goal}: {Path}")