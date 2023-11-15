def solution(n):
    answer = 0
    if n **(1/2) % 1 == 0:
        return 1
    return 2