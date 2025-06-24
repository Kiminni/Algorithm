from collections import deque

N, M = map(int, input().split())

l = []
for _ in range(N):
    line = input().strip()
    row = list(map(int, line))
    l.append(row)  

def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and l[nx][ny] == 1:
                l[nx][ny] = l[x][y] + 1
                queue.append((nx, ny))

    return l[N-1][M-1]

print(BFS(0, 0))