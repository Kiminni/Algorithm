def solution(n, computers):
    num = len(computers)
    visited = [False] * n
    dic = {}
    answer = 0
    
    for i in range(num):
        tmp = []
        for j in range(num):
            if computers[i][j] == 1 and i != j:
                tmp.append(j)
        dic[i] = tmp
        
    for i in range(num):
        if not visited[i]:
            dfs(visited, i, dic)
            answer += 1
    return answer
    
def dfs(visited, cur_v, dic):
    visited[cur_v] = True
    for i in dic[cur_v]:
        if not visited[i]:
            dfs(visited, i, dic)
    
    