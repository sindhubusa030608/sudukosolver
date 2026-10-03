INF = 999
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
    ]
n = len(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )
print("Shortesr distances:")
for row in graph:
    print(row)
