def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 :
            return False
    return True
def solution(numbers):
    answer = 0
    nums = set()
    pick = [False] * len(numbers)
    def recur(current):
        for i in range(len(numbers)):
            if not pick[i]:
                pick[i] = True
                nums.add(current * 10 + int(numbers[i]))
                recur(current * 10 + int(numbers[i]))
                pick[i] = False
    recur(0)
    for num in nums:
        if isPrime(num):
            answer += 1
    return answer