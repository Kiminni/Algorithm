"""
1. 입력 받은 숫자가 짝수면 2로 나눈다.
2. 입력된 숫자가 홀수면 3을 곱하고 1을 더한다.
3. 결과가 1일 때까지 반복 -> 주어진 수가 1이면 0, 총 500번 반복

"""
def solution(num):
    answer = 0
    if num == 1:
        return 0
    
    for i in range(500):
        if num % 2 == 0:
            num = num // 2
        
        elif num == 1:
            break
        
        else:
            num = num * 3 + 1
        
        answer += 1
        
    
    if num == 1:
        return answer
    
    return -1
