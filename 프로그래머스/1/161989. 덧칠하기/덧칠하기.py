def solution(n, m, section):
    answer = 0
    paint = 0
    for value in section:
        if value > paint:
            paint = value + m -1
            answer += 1
    return answer