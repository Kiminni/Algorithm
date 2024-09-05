def solution(n, computers):
    # 초기세팅
    n = len(computers)
    answer = 0
    graph = {}
    visited = [False] * n
    for i in range(n):
        graph[i] = [] 
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    # 모든 vertex에 대해서 방문한적 없으면 dfs 실행하고 count += 1
    for cur_v in range(n):
        if not visited[cur_v]:
            #bfs()
            dfs(cur_v, graph, visited)
            answer += 1

    
    return answer

def dfs(cur_v, graph, visited):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v, graph, visited)