# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input("정수 a를 입력하세요.: "))
b = int(input("정수 b를 입력하세요.: "))

if a > b:
    a,b = b,a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end = '') #합 구하는 과정 출력
    else:
        print(f'{i} = ', end = '')
    sum += i

print(sum)

# 비효율적 -> 10000번 실행된다고 가정할 시 13행 9999번 실행, 15행 1번 실행