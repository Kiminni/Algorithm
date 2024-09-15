from itertools import permutations
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    n = len(numbers)
    nums = set()
    picked = [False] * n
    answer = 0
    temp = []
    for i in range(1, n + 1):
         temp += list(set(permutations(numbers, i)))
    print(temp)
    for t in temp:
        if isPrime(int(''.join(t))):
            if t[0] =="0":
                continue
            answer += 1
    
    # def permute(cur_number):
    #     for i in range(n):
    #         if not picked[i]:
    #             picked[i] = True
    #             nums.add(cur_number * 10 + int(numbers[i]))
    #             permute(cur_number * 10 + int(numbers[i]))
    #             picked[i] = False
    # permute(0)        
    
    for num in nums:
        if isPrime(num):
            answer += 1
            
    return answer
            
        