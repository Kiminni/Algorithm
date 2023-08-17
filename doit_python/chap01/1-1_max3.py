# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다')

a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))

maximum = a
if maximum < b:
    maximum = b
if maximum < c:
    maximum = c

print(maximum)