import heapq

class GrafoDijkstra:
    
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.arestas = {}
        self.vertices = {}
    
    def adicionar_vertice(self, id_vertice, nome):
        self.vertices[id_vertice] = nome
        if id_vertice not in self.arestas:
            self.arestas[id_vertice] = []
    
    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.arestas:
            self.arestas[origem] = []
        self.arestas[origem].append((destino, peso))
    
    def dijkstra(self, origem):
        distancia = {}
        predecessor = {}
        
        for v in range(self.V):
            distancia[v] = float('inf')
            predecessor[v] = None
        
        distancia[origem] = 0
        
        fila_prioridade = [(0, origem)]
        visitados = set()
        
        while fila_prioridade:
            dist_atual, vertice_atual = heapq.heappop(fila_prioridade)
            
            if vertice_atual in visitados:
                continue
            
            visitados.add(vertice_atual)
            
            if vertice_atual in self.arestas:
                for vizinho, peso in self.arestas[vertice_atual]:
                    nova_distancia = distancia[vertice_atual] + peso
                    
                    if nova_distancia < distancia[vizinho]:
                        distancia[vizinho] = nova_distancia
                        predecessor[vizinho] = vertice_atual
                        heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
        
        return distancia, predecessor
    
    def construir_caminho(self, origem, destino, predecessor):
        if predecessor[destino] is None and origem != destino:
            return None
        
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            atual = predecessor[atual]
        
        caminho.reverse()
        return caminho
    
    def imprimir_resultados(self, origem, distancia, predecessor):
        print(f"\nOrigem: {self.vertices[origem]}")
        print(f"{'Destino':<25} {'Distância':<15} {'Caminho'}")
        print("-" * 70)
        
        for v in range(self.V):
            if distancia[v] == float('inf'):
                caminho_str = "Inalcançável"
                dist_str = "∞"
            else:
                caminho = self.construir_caminho(origem, v, predecessor)
                caminho_str = " → ".join(self.vertices[c] for c in caminho)
                dist_str = f"{distancia[v]:.1f} km"
            
            print(f"{self.vertices[v]:<25} {dist_str:<15} {caminho_str}")


def exemplo_sistema_transporte():
    grafo = GrafoDijkstra(16)
    
    estacoes = {
        0: "Centro", 1: "Zona Norte", 2: "Zona Sul", 3: "Zona Leste",
        4: "Zona Oeste", 5: "Aeroporto", 6: "Rodoviária", 7: "Porto",
        8: "Universidade", 9: "Hospital Central", 10: "Shopping Downtown",
        11: "Parque Industrial", 12: "Estádio", 13: "Praia",
        14: "Montanha", 15: "Vila Histórica"
    }
    
    for id_estacao, nome in estacoes.items():
        grafo.adicionar_vertice(id_estacao, nome)
    
    rotas = [
        (0, 1, 8.5), (0, 2, 6.2), (0, 3, 7.0), (0, 10, 3.5),
        (1, 0, 8.5), (1, 6, 5.0), (1, 11, 9.0),
        (2, 0, 6.2), (2, 13, 4.0), (2, 7, 8.0), (2, 10, 2.5),
        (3, 0, 7.0), (3, 5, 12.0), (3, 8, 6.5),
        (4, 0, 9.0), (4, 14, 15.0), (4, 11, 7.5),
        (5, 3, 12.0), (5, 6, 8.0), (5, 1, 3.0),
        (6, 1, 5.0), (6, 5, 8.0), (6, 11, 6.0),
        (7, 2, 8.0), (7, 13, 5.5), (7, 15, 10.0),
        (8, 3, 6.5), (8, 9, 4.0), (8, 12, 7.0),
        (9, 8, 4.0), (9, 0, 5.5), (9, 10, 3.0),
        (10, 0, 3.5), (10, 9, 3.0), (10, 12, 8.5),
        (11, 1, 9.0), (11, 4, 7.5), (11, 6, 6.0), (11, 14, 4.0),
        (12, 8, 7.0), (12, 10, 8.5), (12, 13, 6.0),
        (13, 2, 4.0), (13, 7, 5.5), (13, 12, 6.0), (13, 15, 2.0),
        (14, 4, 15.0), (14, 11, 10.0), (14, 15, 8.0),
        (15, 7, 10.0), (15, 13, 7.0), (15, 14, 8.0),
    ]
    
    print("\nALGORITMO DE DIJKSTRA - Sistema de Transporte")
    
    for origem, destino, peso in rotas:
        grafo.adicionar_aresta(origem, destino, peso)
    
    origem = 0
    distancia, predecessor = grafo.dijkstra(origem)
    grafo.imprimir_resultados(origem, distancia, predecessor)
    
    print("\n" + "="*70)
    origem2 = 5
    distancia2, predecessor2 = grafo.dijkstra(origem2)
    grafo.imprimir_resultados(origem2, distancia2, predecessor2)


if __name__ == "__main__":
    exemplo_sistema_transporte()
