def solution(numbers):
    answer = numbers[0] * numbers[1]
    for i in numbers:
        for j in numbers:
            if j == i :
                continue
            if i * j >= answer:
                answer = i * j
    return answer