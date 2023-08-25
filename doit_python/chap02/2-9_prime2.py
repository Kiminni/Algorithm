# 1,000 이하의 소수 나열하기(알고리즘 개선 1)

counter = 0 # 나눗셈 횟수
ptr = 0 # 찾은 개수
prime = [None] * 500 # 소수 저장 배열

prime[ptr] = 2 # 초기값 2
ptr += 1

for n in range(3, 1001, 2): # 홀수만을 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님 
            break # 처음으로
        
    else:
        prime[ptr] = n # 끝까지 버텼다면 소수로 처리
        ptr += 1 #소수 개수 1 증가
    
for i in range(ptr): # ptr의 소수 출력
    print(prime[i]) # 
print(f'나눗셈을 실행한 횟수: {counter}')

# 첫 번째 for문 -> 홀수만 나누도록
# 두 번째 for문 -> 내부의 prime 배열에서 처리하기 위해 1부터 ptr 인덱스를 증가시켜가며 prime 배열의 수를 나눔

    
