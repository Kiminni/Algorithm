def solution(n, computers):
    answer = 0
    n = len(computers)
    graph = {}
    visited = [False] * n
    
    for i in range(n):
        tmp = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                tmp.append(j)
            graph[i] = tmp
    
    for k in range(n):
        if not visited[k]:
            dfs(visited, graph, k)
            answer += 1
    
    return answer
    
def dfs(visited, graph, cur_v):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(visited, graph, next_v)