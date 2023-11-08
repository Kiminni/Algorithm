def solution(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp = tmp * i
        if tmp > n:
            return i - 1
    return i