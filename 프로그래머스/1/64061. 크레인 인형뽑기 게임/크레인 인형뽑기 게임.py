def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move = move - 1
        for i in range(len(board)):
            if board[i][move] > 0 :
                stack.append(board[i][move])
                board[i][move] = 0
                if len(stack) > 1 and stack[len(stack) - 1] == stack[len(stack) - 2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer