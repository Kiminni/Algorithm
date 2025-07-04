from collections import deque
import sys
input = sys.stdin.readline  # 빠른 입력

M, N = map(int, input().split())
box = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    box.append(tmp)

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))


def bfs():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

bfs()

day = 0
for row in box:
    for i in row:
        if i == 0:
            print(-1)
            sys.exit() 
    day = max(day, max(row))

print(day - 1)