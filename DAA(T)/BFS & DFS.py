#DFS
"""graph={'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':['A','C'],
    'E':['B','C']
}
visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')"""

#BFS
graph={'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[]
}
visited=set()
def bfs(visited,graph,root):
    queue=[root]
    while queue:
        current=queue.pop(0)
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
bfs(visited,graph,'A')
