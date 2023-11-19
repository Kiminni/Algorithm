def solution(board):
    answer = 0
    N = len(board)
    boom = []
    
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    
    # 지뢰 위치 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                boom.append((i,j))
    
    # 위험 지역 표시
    for x,y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1
    
    # 안전 지대
    for a in range(N):
        for b in range(N):
            if board[a][b] == 0:
                answer += 1
    return answer
    
        