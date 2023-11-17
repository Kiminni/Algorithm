def solution(keyinput, board):
    tmp = [0,0]
    for key in keyinput:
        if key == "left":
            tmp[0] -= 1
        elif key == "right":
            tmp[0] += 1
        elif key == "up":
            tmp[1] += 1
        else: 
            tmp[1] -= 1
            
        if board[1] // 2 < abs(tmp[1]):
            if tmp[1] > 0:
                tmp[1] = (board[1] // 2)
            else:
                tmp[1] = -(board[1] // 2)

        if board[0] // 2 < abs(tmp[0]):
            if tmp[0] > 0:
                tmp[0] = (board[0] // 2)
            else:
                tmp[0] = -(board[0] // 2)
    
    
    
    return tmp