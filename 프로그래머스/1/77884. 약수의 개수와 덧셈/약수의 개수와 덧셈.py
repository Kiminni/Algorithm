# left, right 주어진다.
# left -> right 까지의 모든 수 중에서, 약수의 개수가 짝수면 더한다. 그리고, 홀수면 뺀다.
"""
1. 13 = 1, 13
2. 14 = 1, 2, 7, 14
3. 15 = 1, 3, 5, 15
4. 16 = 1, 2, 4, 8, 16
5. 17 = 1, 17

# left ~ right 로 반복문을 실행합니다.
# 이제 약수의 개수를 확인합니다.
# 보게 되면, 이제 홀수 = 제곱수 일 때만이니까.
"""
def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        if int(number ** 0.5) ** 2 == number:
            answer -= number
        else:
            answer += number
        
    

    return answer