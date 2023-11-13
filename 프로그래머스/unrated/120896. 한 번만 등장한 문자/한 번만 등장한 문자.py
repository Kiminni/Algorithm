def solution(s):
    answer = []

    for i in s:
        if s.count(i) == 1:
            answer.append(i)
    print(answer)
    answer.sort()
    return ''.join(answer)