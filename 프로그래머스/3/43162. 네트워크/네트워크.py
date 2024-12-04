def solution(n, computers):
    n = len(computers)
    graph = {}
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        tmp = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                tmp.append(j)
        graph[i] = tmp
    
    for i in range(n):
        if not visited[i]:
            dfs(visited, graph, i)
            answer += 1    
    return answer

        
def dfs(visited, graph, cur_v):
    visited[cur_v] = True
    for i in graph[cur_v]:
        if not visited[i]:
            dfs(visited, graph, i)