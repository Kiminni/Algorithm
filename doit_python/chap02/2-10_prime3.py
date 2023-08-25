# 1,000 이하의 소수를 나열하기(알고리즘 개선 2)

# 직사각형이라면, 한 변의 길이만 나눗셈을 시도하고 그래도 나누어지지 않으면 소수라고 생각해도 무방하다
# n의 제곱근 이하의 어떤 소수도 나누어 떨어지지 않는다.

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

counter_mul = 0
counter_div = 0

for n in range(5, 1000, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2 # 곱셈 한 번, 나눗셈 한 번 해서 + 2
        counter_mul += 1
        counter_div += 1
        if n % prime[i] == 0 :
            break
        
        i += 1
        
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1
        counter_div += 1

for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
print(f'곱셈을 실행한 횟수: {counter_mul}')
print(f'나눗셈을 실행한 횟수: {counter_div}')
