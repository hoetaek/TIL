import heapq

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))
    distance = dijkstra(N, graph, 1)
    answer = [i for i, dist in enumerate(distance) if dist <= K]

    return answer

def dijkstra(N, graph, start):
    q = []
    INF = int(1e9)
    distance = [INF for _ in range(N+1)]
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance
          
s = solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
print(s)