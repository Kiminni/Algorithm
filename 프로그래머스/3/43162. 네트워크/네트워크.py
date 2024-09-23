def solution(n, computers):
    graph = {}
    answer = 0
    n = len(computers)
    visited = [False] * n
    for i in range(n):
        tmp = []
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                tmp.append(j)
        graph[i] = tmp
    for current in graph:
        if not visited[current]:
            dfs(current, visited, graph)
            answer += 1
            
            
    
    return answer


def dfs(cur_v, visited, graph):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            visited[next_v] = True    
            dfs(next_v, visited, graph)
            
        