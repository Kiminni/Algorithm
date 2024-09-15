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
    
    def permute(cur_number):
        for i in range(n):
            if not picked[i]:
                picked[i] = True
                nums.add(cur_number * 10 + int(numbers[i]))
                permute(cur_number * 10 + int(numbers[i]))
                picked[i] = False
    permute(0)        
    
    for num in nums:
        if isPrime(num):
            answer += 1
            
    return answer
            
        