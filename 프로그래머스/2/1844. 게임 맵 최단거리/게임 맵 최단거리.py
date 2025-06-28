from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] =  maps[x][y] + 1
                queue.append((nx, ny))
        
    answer = maps[n-1][m-1]
    if answer == 1:
        return -1
    return answer