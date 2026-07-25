# MLA0104 - Artificial Intelligence and Expert Systems (AIES) Experiments

This repository contains implementations of core AI search and game-playing algorithms completed as part of the MLA0104 - AIES course.

---

## 1. Breadth First Search (BFS)

```
BFS(graph, start, goal):
    queue = [start]
    visited = {start}

    while queue is not empty:
        node = queue.dequeue()
        if node == goal: return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
```

---

## 2. Depth First Search (DFS)

```
DFS(graph, node, goal, visited = {}):
    visited.add(node)
    if node == goal: return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, goal, visited)
```

---

## 3. Uniform Cost Search (UCS)

```
UCS(graph, start, goal):
    PQ = [(0, start)]     // (cost, node)
    visited = {}

    while PQ not empty:
        cost, node = PQ.pop_min()
        if node == goal: return cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                PQ.insert((cost + edge_cost, neighbor))
```

---

## 4. Water Jug Problem

```
WaterJug(cap1, cap2, target):
    queue = [(0, 0)]
    visited = {(0,0)}

    while queue not empty:
        j1, j2 = queue.dequeue()
        if j1 == target or j2 == target: return solved

        states = [(cap1,j2), (j1,cap2), (0,j2), (j1,0),
                  pour(j1->j2), pour(j2->j1)]

        for s in states:
            if s not in visited:
                visited.add(s)
                queue.enqueue(s)
```

---

## 5. A* Search Algorithm

```
A_Star(graph, start, goal, h):
    OPEN = [(h[start], start)]
    g = {start: 0}

    while OPEN not empty:
        f, node = OPEN.pop_min()
        if node == goal: return path

        for neighbor, cost in graph[node]:
            temp_g = g[node] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                OPEN.insert((temp_g + h[neighbor], neighbor))
```

---

## 6. Alpha-Beta Pruning

```
AlphaBeta(node, depth, alpha, beta, isMax):
    if depth == 0 or node is terminal: return evaluate(node)

    if isMax:
        best = -INF
        for child in node.children:
            best = max(best, AlphaBeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = +INF
        for child in node.children:
            best = min(best, AlphaBeta(child, depth-1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha: break
        return best
```

---

## 7. Minimax Algorithm

```
Minimax(node, depth, isMax):
    if depth == 0 or node is terminal: return evaluate(node)

    if isMax:
        return max(Minimax(child, depth-1, False) for child in node.children)
    else:
        return min(Minimax(child, depth-1, True) for child in node.children)
```

---

## 8. Greedy Best First Search (GBFS)

```
GBFS(graph, start, goal, h):
    PQ = [(h[start], start)]
    visited = {}

    while PQ not empty:
        _, node = PQ.pop_min()
        if node == goal: return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                PQ.insert((h[neighbor], neighbor))
```

---

## Author

**Yash Sharma**
SIMATS Engineering
Course: MLA0104 - Artificial Intelligence and Expert Systems
