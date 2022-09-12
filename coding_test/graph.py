from pprint import pprint

def solution(n, results):
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        graph[a][a] = 0
    
    for i in range(len(results)):
        graph[results[i][0]][results[i][1]] = 1
        graph[results[i][1]][results[i][0]] = -1
    # pprint(graph)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] * graph[k][b] == 1:
                    graph[a][b] = graph[a][k]
                
                
    # pprint(graph)
    answer = 0
    for g in graph:
        count = 0
        count += sum(i == 1 or i == -1 for i in g)
        if count == n - 1:
            answer += 1
    return answer

def get_final_r(players, player, visited, n, count=0):
    if count == n - 1:
        print()
        return True
    elif all(visited[1:]):
        return False
    
    for i in range(len(players)):
        already_played = players[i]
        for p in already_played:
            if visited[p] is False:
                visited[p] = True
                return get_final_r(players, visited, n, count + 1)
        

    return players
"""
def ex():
    n = 1
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n +1):
            if a == b:
                graph[a][b] = 0
    
    for i in range(len(results)):
        graph[results[i][0]][results[i][1]] = 1
        graph[results[i][1]][results[i][0]] = 1
    pprint(graph)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a != INF and b != INF:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    

    return graph
    """
    
    
# s = solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
s = solution(5, [[1, 2], [4, 5], [3, 4], [2, 3]])
# s = solution(6,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [6, 5]])
# s = solution(3,	[[3, 1], [3, 2], [2, 1]])
pprint(s)