def solution(n):
    answer = n
    if n % 7 == 0:
        return n / 7
    return n // 7 + 1