from collections import deque, defaultdict
from typing import List, Dict, Optional

def bfs_shortest_path(graph: Dict[str, List[str]], start: str, end: str) -> Optional[List[str]]:
#Находит кратчайший путь от start до end в графе с использованием BFS

    # Очередь для BFS (хранит вершины для обработки)
    queue = deque()
    # Для отслеживания посещенных вершин
    visited = set()
    # Для восстановления пути (хранит родительскую вершину для каждой)
    parent = {}
    
    # Начинаем с начальной вершины
    queue.append(start)
    visited.add(start)
    parent[start] = None  # У начальной вершины нет родителя
    
    # Основной цикл BFS
    while queue:
        current = queue.popleft()
        
        # Если достигли конечной вершины
        if current == end:
            # Восстанавливаем путь от конца к началу
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            # Разворачиваем путь, так как мы шли от конца к началу
            return path[::-1]
        
        # Проходим по всем соседям текущей вершины
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
    
    # Если путь не найден
    return None

def build_maze_graph() -> Dict[str, List[str]]:
#Создает граф лабиринта на основе рисунка

    # Граф представляется как словарь:
    # ключ - вершина (комната), значение - список смежных вершин
    graph = {
        'S': ['A', 'B', 'C'],      # S соединена с A, B, C
        'A': ['S', 'D'],           # A соединена с S, D
        'B': ['S', 'D', 'E', 'C'], # B соединена с S, D, E, C
        'C': ['S', 'B', 'F', 'J'], # C соединена с S, B, F, J
        'D': ['A', 'B', 'G'],      # D соединена с A, B, G
        'E': ['B', 'H'],           # E соединена с B, H
        'F': ['C', 'I'],           # F соединена с C, I
        'G': ['D', 'H'],           # G соединена с D, H
        'H': ['E', 'G'],           # H соединена с E, G
        'I': ['F', 'J'],           # I соединена с F, J
        'J': ['C', 'I']            # J соединена с C, I
    }
    return graph

def visualize_graph(graph: Dict[str, List[str]]) -> None:
#Визуализирует граф лабиринта
    print("\n" + "="*50)
      
    for room, neighbors in sorted(graph.items()):
        print(f"  {room}: {', '.join(sorted(neighbors))}")
    
    print("""
        A --- D --- G
         \\   / \\   /
          \\ /   \\ /
           S --- B --- E --- H
          / \\   / \\         /
         /   \\ /   \\       /
        C --- F --- J --- I
         \\         /
          \\       /
           \\     /
            \\   /
             \\ /
    """)
