def solution(numbers):
    answer = 0
    nums = set()
    n = len(numbers)
    picked = [False] * n
    
    def recur(current):
        for i in range(n):
            if not picked[i]:
                picked[i] = True
                nums.add(current * 10 + int(numbers[i]))
                recur(current * 10 + int(numbers[i]))
                picked[i] = False
    recur(0)
    
    for num in nums:
        if prime(num):
            answer += 1
    return answer

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True