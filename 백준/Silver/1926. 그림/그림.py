from collections import deque
N, M = map(int, input().split())
l = []

for i in range(N):
    tmp = list(map(int, input().split()))
    l.append(tmp)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

paint = []
for i in range(N):
    for j in range(M):
        if l[i][j] == 1:
            paint.append(bfs(l, i, j))

if len(paint) == 0:
    print(0)
    print(0)

else:
    print(len(paint))
    print(max(paint))