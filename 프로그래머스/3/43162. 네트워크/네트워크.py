def solution(n, computers):
    graph = {}
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        tmp = []
        for j in range(n):
            if computers[i][j] == 1 and i != j :
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