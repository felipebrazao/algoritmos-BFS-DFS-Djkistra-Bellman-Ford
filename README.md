# Algoritmos de Busca e Caminho Mínimo em Grafos

Este projeto contém implementações em Python de algoritmos clássicos de teoria dos grafos para busca e cálculo de caminhos mínimos.

## Algoritmos Implementados

### BFS (Breadth-First Search)

Localização: `bfs/bfs.py`

O algoritmo de Busca em Largura explora os vértices de um grafo nível por nível, começando de um vértice inicial. É útil para encontrar o caminho mais curto em grafos não ponderados.

Funcionalidades:
- Travessia completa do grafo
- Encontrar caminho mais curto entre dois vértices
- Análise de acessibilidade da rede

Exemplo de uso:
```bash
python bfs/bfs.py
```

### DFS (Depth-First Search)

Localização: `DFS/main.py`

O algoritmo de Busca em Profundidade explora o grafo seguindo um caminho até o fim antes de retroceder. O projeto inclui duas versões:
- Versão recursiva
- Versão iterativa (usando pilha)

Exemplo de uso:
```bash
python DFS/main.py
```

### Bellman-Ford

Localização: `bellman_ford.py`

O algoritmo de Bellman-Ford encontra o caminho mais curto de um vértice de origem para todos os outros vértices, mesmo em grafos com arestas de peso negativo. Também detecta ciclos negativos.

Funcionalidades:
- Cálculo de distâncias mínimas
- Construção de caminhos
- Detecção de ciclos negativos

Exemplo de uso:
```bash
python bellman_ford.py
```

## Requisitos

- Python 3.x

## Estrutura do Projeto

```
.
├── bfs/
│   └── bfs.py
├── DFS/
│   └── main.py
├── bellman_ford.py
└── README.md
```

## Exemplos de Aplicação

Os algoritmos são demonstrados através de casos de uso em sistemas de transporte urbano:

- **BFS**: Navegação em rede de transporte metropolitano com 16 estações
- **DFS**: Exploração de grafos simples
- **Bellman-Ford**: Sistema de rotas com distâncias entre estações
