def solution(n, computers):
    graph = {}
    answer = 0
    n = len(computers)
    visited = [False] * n
    for i in range(n):
        tmp = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                tmp.append(j)
        graph[i] = tmp
    print(visited)
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            answer += 1
    return answer

def dfs(cur_v, visited, graph):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v, visited, graph)