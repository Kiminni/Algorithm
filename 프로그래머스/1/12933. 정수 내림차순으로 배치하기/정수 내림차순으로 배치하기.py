def solution(n):
    list_n = sorted(list(str(n)),reverse=True)
    return int(''.join(list_n))