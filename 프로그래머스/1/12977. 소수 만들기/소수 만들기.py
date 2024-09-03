from itertools import combinations

def isPrime(n):
	if n < 2:
        return False
    
    for i in range (2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    comb = combinations(nums, 3)
    for c in comb:
        a = sum(c)
        if isPrime(n):
            answer += 1
    
    return answer