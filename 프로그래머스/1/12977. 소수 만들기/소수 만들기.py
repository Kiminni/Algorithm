from itertools import combinations

def solution(nums):
    def isPrime(n):
        for i in range(2, int(n **0.5) + 1):
            if n % i == 0 :
                return False
        return True
    answer = 0
    com = combinations(nums, 3)
    for c in com:
        tmp = sum(c)
        if isPrime(tmp):
            answer += 1
    return answer