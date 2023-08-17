# 1부터 n까지 정수의 합 출력하기(n은 양수만)

print('1부터 n까지 정수의 합을 출력합니다.')

while True:
    n = int(input("n을 입력하세요: "))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f'1부터 {n}까지의 합은 {sum}입니다.')

'''
while i<= n : => i = n + 1 (종료 시)
for i in range(시작값, n + 1): => i = n(종료시)
'''