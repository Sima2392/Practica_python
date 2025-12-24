import heapq

def dijkstra(n, s, f, graph):
    # Инициализация расстояний
    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0
    
    # Минимальная куча (приоритетная очередь)
    pq = [(0, s)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Если извлеченное расстояние больше текущего, пропускаем
        if current_dist > dist[u]:
            continue
            
        # Перебираем всех соседей вершины u
        for v in range(n):
            if graph[u][v] >= 0:  # Есть ребро
                weight = graph[u][v]
                new_dist = current_dist + weight
                
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    return dist[f] if dist[f] != INF else -1



def min_cost_path(n, prices, roads):
    # Создаем список смежности
    adj = [[] for _ in range(n)]
    
    # Добавляем дороги в обе стороны (граф неориентированный)
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    
    # Инициализация
    INF = float('inf')
    cost = [INF] * n
    cost[0] = prices[0]
    
    # Минимальная куча (стоимость, город)
    pq = [(prices[0], 0)]
    
    while pq:
        current_cost, u = heapq.heappop(pq)
        
        # Если дошли до конечного города
        if u == n - 1:
            return current_cost
            
        # Если извлеченная стоимость больше текущей, пропускаем
        if current_cost > cost[u]:
            continue
            
        # Перебираем соседей
        for v in adj[u]:
            # Стоимость добраться до соседнего города
            new_cost = current_cost + prices[v]
            
            if new_cost < cost[v]:
                cost[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    
    return -1