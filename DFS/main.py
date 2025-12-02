
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# -------------------------------
# DFS RECURSIVO
# -------------------------------
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")      # Mostra o nó visitado
    visited.add(node)         # Marca como visitado

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# -------------------------------
# DFS ITERATIVO (COM PILHA)
# -------------------------------
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]        # Começa colocando o nó inicial na pilha

    while stack:
        node = stack.pop()  # Remove o último elemento (profundidade)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Adiciona vizinhos na pilha (invertido para manter ordem)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

print("DFS Recursivo:")
dfs_recursive(graph, 'A')

print("\n\nDFS Iterativo:")
dfs_iterative(graph, 'A')
