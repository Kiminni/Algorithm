from collections import deque
N,M = map(int, input().split())
maps = []
for i in range(N):
    tmp = input().strip()  # 문자열 그대로
    l = list(map(int, tmp))  # 문자열의 각 문자를 숫자로 변환
    maps.append(l)
def bfs(x, y, graph):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    answer = graph[N-1][M-1]
    return answer

print(bfs(0, 0, maps))