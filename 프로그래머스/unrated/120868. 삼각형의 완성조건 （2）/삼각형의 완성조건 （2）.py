def solution(sides):
    answer = 0
    sides.sort()
    for i in range(1, max(sides) + 1):
        if i + sides[0] > max(sides):
            answer += 1
    
    for j in range(max(sides) + 1, sum(sides) + 1):
        if sum(sides) > j:
            answer += 1
    return answer