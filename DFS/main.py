graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['J', 'K'],
    'G': ['L'],
    'H': ['M'],
    'I': ['M', 'N'],
    'J': ['O'],
    'K': ['O', 'P'],
    'L': ['P'],
    'M': [],
    'N': ['P'],
    'O': [],
    'P': []
}

# -------------------------------
# DFS RECURSIVO
# -------------------------------
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")      
    visited.add(node)         

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# -------------------------------
# DFS ITERATIVO (COM PILHA)
# -------------------------------
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


print("DFS Recursivo:")
dfs_recursive(graph, 'A')

print("\n\nDFS Iterativo:")
dfs_iterative(graph, 'A')
