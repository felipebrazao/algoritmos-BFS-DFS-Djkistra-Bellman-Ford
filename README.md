# 📊 Algoritmos de Grafos - BFS, DFS, Dijkstra e Bellman-Ford

Implementação de algoritmos clássicos de busca e caminhos mínimos em grafos, utilizando contextos práticos para facilitar o entendimento.

---

## 🚀 Algoritmos Implementados

### 1. **BFS - Busca em Largura** (`BFS/`)
Explora o grafo nível por nível, visitando todos os vizinhos antes de avançar.

**Características:**
- 📊 Usa fila (FIFO)
- ✅ Encontra o caminho mais curto em grafos não ponderados
- 🎯 Complexidade: O(V + E)
- 📦 Ideal para encontrar menor número de arestas

**Quando usar:**
- Encontrar menor distância em grafos sem peso
- Verificar se um grafo é conexo
- Encontrar componentes conectados
- Problemas de menor número de passos

### 2. **DFS - Busca em Profundidade** (`DFS/`)
Explora o grafo indo o mais fundo possível antes de retroceder.

**Características:**
- 📚 Usa pilha (LIFO) ou recursão
- ✅ Explora um caminho completamente antes de outros
- 🎯 Complexidade: O(V + E)
- 📦 Ideal para detecção de ciclos e ordenação topológica

**Quando usar:**
- Detectar ciclos em grafos
- Ordenação topológica
- Encontrar componentes fortemente conectados
- Resolver labirintos e puzzles

### 3. **Bellman-Ford** (`bellman_ford.py`)
Encontra caminhos mais curtos mesmo com **arestas de peso negativo**.

**Características:**
- ✅ Funciona com pesos negativos
- ✅ Detecta ciclos negativos
- 🐢 Complexidade: O(V × E)
- 📦 Usa lista de arestas

**Quando usar:**
- Grafos com arestas negativas (descontos, promoções)
- Necessidade de detectar ciclos negativos
- Arbitragem, sistemas com economias

### 4. **Dijkstra** (`dijkstra.py`)
Encontra caminhos mais curtos de forma **otimizada** usando fila de prioridade.

**Características:**
- ❌ Não funciona com pesos negativos
- ⚡ Complexidade: O(E log V)
- 📦 Usa lista de adjacências + heap
- 🎯 Estratégia gulosa

**Quando usar:**
- Grafos sem pesos negativos
- Necessidade de alta performance
- GPS, roteamento de redes, mapas

---

## 📍 Contexto: Sistema de Transporte Urbano

**16 Estações:**
- Centro
- Zona Norte, Sul, Leste, Oeste
- Aeroporto
- Rodoviária
- Porto
- Universidade
- Hospital Central
- Shopping Downtown
- Parque Industrial
- Estádio
- Praia
- Montanha
- Vila Histórica

### 🛣️ Arestas Especiais no Bellman-Ford

O código do Bellman-Ford inclui **4 rotas com peso negativo** representando túneis expressos e declives:

- Zona Sul → Shopping: **-2.5 km** (túnel expresso)
- Aeroporto → Zona Norte: **-3.0 km** (via expressa com declive)
- Parque Industrial → Montanha: **-4.0 km** (descida íngreme)
- Praia → Vila Histórica: **-2.0 km** (túnel costeiro)

> 💡 No Dijkstra, esses pesos foram convertidos para positivos, pois o algoritmo não suporta arestas negativas.

---

## 🖥️ Como Executar

### BFS:
```bash
cd BFS
python main.py
```

### DFS:
```bash
cd DFS
python main.py
```

### Bellman-Ford:
```bash
python bellman_ford.py
```

### Dijkstra:
```bash
python dijkstra.py
```

---

## 📊 Saída dos Programas

Ambos os programas executam o algoritmo **duas vezes**:
1. A partir do **Centro**
2. A partir do **Aeroporto**

### Exemplo de Saída:
```
Origem: Centro
Destino                   Distância       Caminho
----------------------------------------------------------------------
Centro                    0.0 km          Centro
Zona Norte                8.5 km          Centro → Zona Norte
Shopping Downtown         3.5 km          Centro → Shopping Downtown
...
```

---

## 🔍 Comparação entre os Algoritmos

| Aspecto | BFS | DFS | Dijkstra | Bellman-Ford |
|---------|-----|-----|----------|--------------|
| **Propósito** | Busca em largura | Busca em profundidade | Caminho mínimo | Caminho mínimo |
| **Estrutura** | Fila (FIFO) | Pilha/Recursão | Heap | Lista de arestas |
| **Pesos** | Não considera | Não considera | Apenas positivos | Aceita negativos |
| **Ciclos negativos** | N/A | Detecta ciclos | ❌ Não | ✅ Detecta |
| **Complexidade** | O(V + E) | O(V + E) | O(E log V) | O(V × E) |
| **Velocidade** | ⚡ Rápido | ⚡ Rápido | ⚡ Rápido | 🐢 Lento |
| **Caminho mais curto** | ✅ Sem pesos | ❌ Não garante | ✅ Com pesos positivos | ✅ Com pesos quaisquer |

---

## 📚 Estrutura do Código

### BFS:
```python
class Grafo:
    - bfs(origem)               # Busca em largura usando fila
    - imprimir_resultados()     # Exibe ordem de visitação
```

### DFS:
```python
class Grafo:
    - dfs(origem)               # Busca em profundidade (iterativa ou recursiva)
    - imprimir_resultados()     # Exibe ordem de visitação
```

### Bellman-Ford:
```python
class GrafoBellmanFord:
    - bellman_ford(origem)      # Algoritmo principal
    - construir_caminho()        # Reconstrói rota
    - imprimir_resultados()      # Exibe tabela formatada
```

### Dijkstra:
```python
class GrafoDijkstra:
    - dijkstra(origem)          # Algoritmo com heap
    - construir_caminho()        # Reconstrói rota
    - imprimir_resultados()      # Exibe tabela formatada
```

---

## 🎯 Conceitos Importantes

### Busca em Largura (BFS)
Visita vértices nível por nível usando fila:
```python
fila = [origem]
while fila:
    vertice = fila.pop(0)
    for vizinho in adjacencias[vertice]:
        fila.append(vizinho)
```

### Busca em Profundidade (DFS)
Explora um caminho completamente antes de retroceder:
```python
pilha = [origem]
while pilha:
    vertice = pilha.pop()
    for vizinho in adjacencias[vertice]:
        pilha.append(vizinho)
```

### Relaxamento de Arestas
Técnica usada por ambos para atualizar distâncias:
```python
Se distancia[origem] + peso < distancia[destino]:
    distancia[destino] = distancia[origem] + peso
    predecessor[destino] = origem
```

### Fila de Prioridade (Dijkstra)
Garante que sempre processa o vértice mais próximo:
```python
heapq.heappush(fila, (distancia, vertice))
```

### Detecção de Ciclo Negativo (Bellman-Ford)
Após V-1 iterações, verifica se ainda há atualizações possíveis:
```python
Se conseguir atualizar após V-1 iterações:
    → Existe ciclo negativo!
```

---

## 📖 Aprendizados

✅ **BFS** é ideal para encontrar caminhos mais curtos em grafos não ponderados  
✅ **DFS** é perfeito para exploração completa e detecção de ciclos  
✅ **Dijkstra** é rápido mas restrito - ideal para grafos com apenas pesos positivos  
✅ **Bellman-Ford** é robusto mas lento - funciona com pesos negativos e detecta ciclos  
✅ Cada algoritmo tem seu propósito específico baseado no tipo de grafo e problema  
✅ BFS e DFS são fundamentais para algoritmos mais complexos  

---

## 👨‍💻 Autor

Implementação didática para estudo de algoritmos de grafos.

---

## 📝 Licença

Livre para uso educacional.
