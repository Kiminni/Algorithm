def solution(n, computers):
    n = len(computers)
    dic = {}
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        tmp = []
        for j in range(n):
            if i !=j and computers[i][j] == 1:
                tmp.append(j)
        dic[i] = tmp
    
    for i in range(n):
        if not visited[i]:
            dfs(visited, i, dic)
            answer += 1
    return answer
    
    
def dfs(visited, cur_v, dic):
    visited[cur_v] = True
    for i in dic[cur_v]:
        if not visited[i]:
            dfs(visited, i, dic)
    
        