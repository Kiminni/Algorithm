def solution(n):
    minimum = []
    for i in range(1, n):
        if n % i == 1:
            minimum.append(i)
    return min(minimum)