# 10~99 사이의 난수(13이 나오면 종료)

import random

n = int(input("난수의 개수를 입력하세요. :"))

for _ in range(n):
    r = random.randint(10,99) # 10~99 사이의 난수 생성
    print(r, end = " ")
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break

else:
    print("\n난수 생성을 종료합니다.")

'''
random.randint(a,b) -> a 이상 b 이하의 정수 중 무작위로 하나를 뽑는 옵션
'''