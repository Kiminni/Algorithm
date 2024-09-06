def solution(n, computers):
    graph = {}
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        tmp = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                tmp.append(j)
            graph[i] = tmp
    
    for cur_v in range(n):
        if not visited[cur_v]:
            dfs(cur_v, visited, graph)
            answer += 1
    return answer


def dfs(cur_v, visited, graph):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v, visited, graph)
    

