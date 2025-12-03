from collections import deque


def bfs_travessia(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    visitados.add(inicio)
    resultado = []
    
    while fila:
        no_atual = fila.popleft()
        resultado.append(no_atual)
        
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    
    return resultado


def bfs_caminho_mais_curto(grafo, origem, destino):
    if origem == destino:
        return [origem], 0
    
    visitados = set()
    fila = deque([(origem, [origem])])
    visitados.add(origem)
    
    while fila:
        no_atual, caminho_atual = fila.popleft()
        
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                novo_caminho = caminho_atual + [vizinho]
                
                if vizinho == destino:
                    num_baldeacoes = len(novo_caminho) - 1
                    return novo_caminho, num_baldeacoes
                
                visitados.add(vizinho)
                fila.append((vizinho, novo_caminho))
    
    return None, float('inf')


def criar_grafo_rede_transporte():
    grafo = {
        'E1': ['E2', 'E7'],
        'E2': ['E1', 'E3', 'E11'],
        'E3': ['E2', 'E4', 'E14'],
        'E4': ['E3', 'E5'],
        'E5': ['E4', 'E6', 'E10'],
        'E6': ['E5'],
        'E7': ['E1', 'E8'],
        'E8': ['E7', 'E9'],
        'E9': ['E8', 'E10'],
        'E10': ['E9', 'E5', 'E13'],
        'E11': ['E2', 'E12'],
        'E12': ['E11', 'E13'],
        'E13': ['E12', 'E10', 'E16'],
        'E14': ['E3', 'E15'],
        'E15': ['E14', 'E16'],
        'E16': ['E15', 'E13']
    }
    
    return grafo


def exibir_informacoes_grafo(grafo):
    num_vertices = len(grafo)
    num_arestas = sum(len(vizinhos) for vizinhos in grafo.values()) // 2
    
    print("=" * 70)
    print("INFORMAÇÕES DA REDE DE TRANSPORTE URBANO")
    print("=" * 70)
    print(f"Número de Estações (Vértices): {num_vertices}")
    print(f"Número de Conexões Diretas (Arestas): {num_arestas}")
    print(f"Grau Médio: {2 * num_arestas / num_vertices:.2f}")
    print()
    
    print("MAPA DA REDE (Lista de Adjacência):")
    print("-" * 70)
    for estacao in sorted(grafo.keys()):
        conexoes = ', '.join(grafo[estacao])
        print(f"{estacao} → [{conexoes}]")
    print("=" * 70)
    print()


if __name__ == "__main__":
    print("\n")
    print("=" * 70)
    print(" SISTEMA DE NAVEGAÇÃO - REDE DE TRANSPORTE URBANO METROPOLITANO")
    print(" Algoritmo: BFS (Breadth-First Search)")
    print("=" * 70)
    print()
    
    grafo_transporte = criar_grafo_rede_transporte()
    exibir_informacoes_grafo(grafo_transporte)
    
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO 1: EXPLORAÇÃO DA REDE A PARTIR DE E1")
    print("=" * 70)
    estacao_inicial = 'E1'
    print(f"Iniciando BFS a partir da estação: {estacao_inicial}")
    print(f"Objetivo: Explorar todas as estações acessíveis\n")
    
    resultado_travessia = bfs_travessia(grafo_transporte, estacao_inicial)
    
    print("Ordem de visitação das estações (nível por nível):")
    print(" → ".join(resultado_travessia))
    print(f"\nTotal de estações alcançadas: {len(resultado_travessia)}")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO 2: ENCONTRAR ROTA MAIS CURTA")
    print("=" * 70)
    
    origem1, destino1 = 'E1', 'E6'
    print(f"\nRota 1: {origem1} (Terminal Leste) → {destino1} (Terminal Oeste)")
    caminho1, baldeacoes1 = bfs_caminho_mais_curto(grafo_transporte, origem1, destino1)
    if caminho1:
        print(f"Caminho encontrado: {' → '.join(caminho1)}")
        print(f"Número de baldeações: {baldeacoes1}")
        print(f"Estações no percurso: {len(caminho1)}")
    
    origem2, destino2 = 'E7', 'E16'
    print(f"\nRota 2: {origem2} (Linha Norte) → {destino2} (Linha Expressa)")
    caminho2, baldeacoes2 = bfs_caminho_mais_curto(grafo_transporte, origem2, destino2)
    if caminho2:
        print(f"Caminho encontrado: {' → '.join(caminho2)}")
        print(f"Número de baldeações: {baldeacoes2}")
        print(f"Estações no percurso: {len(caminho2)}")
    
    origem3, destino3 = 'E11', 'E9'
    print(f"\nRota 3: {origem3} (Linha Sul) → {destino3} (Linha Norte)")
    caminho3, baldeacoes3 = bfs_caminho_mais_curto(grafo_transporte, origem3, destino3)
    if caminho3:
        print(f"Caminho encontrado: {' → '.join(caminho3)}")
        print(f"Número de baldeações: {baldeacoes3}")
        print(f"Estações no percurso: {len(caminho3)}")
    
    print("\n" + "=" * 70)
    
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO 3: ANÁLISE DE ACESSIBILIDADE")
    print("=" * 70)
    print("Verificando quais estações são acessíveis a partir de cada terminal:\n")
    
    terminais = ['E1', 'E6', 'E7', 'E11', 'E14']
    for terminal in terminais:
        estacoes_acessiveis = bfs_travessia(grafo_transporte, terminal)
        print(f"A partir de {terminal}: {len(estacoes_acessiveis)} estações acessíveis")
    
    print("\n" + "=" * 70)
    print("FIM DA DEMONSTRAÇÃO")
    print("=" * 70)
    print()
