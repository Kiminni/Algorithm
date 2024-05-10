"""
dfs인듯?
"""
def solution(board, h, w):
    dy = [0,-1,0,1]
    dx = [-1,0,1,0]
    answer = 0
    color = board[h][w]
    
    for i in range(len(dx)): 
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board): # 범위 내에 존재 하는지
            if board[nx][ny] == color: # 색이 같은지
                answer += 1
    return answer