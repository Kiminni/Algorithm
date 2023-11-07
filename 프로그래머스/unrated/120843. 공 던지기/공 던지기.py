def solution(numbers, k):
    answer = 0
    tmp = 0
    for i in range(k - 1):
        tmp = tmp + 2
        if tmp >= len(numbers):
            tmp = tmp - len(numbers)
        
    return numbers[tmp]