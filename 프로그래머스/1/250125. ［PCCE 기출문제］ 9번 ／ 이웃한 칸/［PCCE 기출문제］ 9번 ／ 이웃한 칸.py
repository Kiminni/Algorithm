"""
dfs인듯?
"""
def solution(board, h, w):
    dh = [0,1,-1,0]
    dw = [-1,0,0,1]
    answer = 0
    color = board[h][w]
    
    for i in range(len(dh)):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[h][w] == board[nh][nw]:
                answer += 1
    return answer