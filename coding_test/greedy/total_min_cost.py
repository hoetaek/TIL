INF = int(1e9)

def solution(n, costs):
    graph = [[] for _ in range(n + 1)]
    for cost in costs:
        node = cost[0]
        target = cost[1]
        c = cost[2]
        graph[node].append((target, c))
        graph[target].append((node, c))
        
    min_cost = INF
    for i in range(n):
        min_cost = min(min_cost, dfs(graph, i, n))
    
    return min_cost


def dfs(graph, start, n):
    total_cost = 0
    visited = [False] * n
    now = start
    
    
    while not all(visited):
        visited[now] = True
        lowest = INF
        for i in graph[now]:
            if visited[i[0]] == True:
                continue
            if lowest > i[1]:
                lowest = i[1]
                now = i[0]
        if lowest != INF:
            total_cost += lowest
    return total_cost

s = solution(n=4, costs=[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
print(s)