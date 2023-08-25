# 1,000 이하의 소수를 나열하기

counter = 0

for n in range(2, 1001): # 2부터 1000까지 도는데
    for i in range(2, n): # 2부터 약수가 있는지 확인
        counter += 1
        if n % i == 0 : # 나눠지면 스탑
            break
    else: # 나누어 떨어지지 않으면 출력
        print(n)

print(f'나눗셈을 실행한 횟수: {counter}')


