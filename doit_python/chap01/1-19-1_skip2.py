# 1부터 12까지 8을 건너뛰고 출력하기 2

for i in list(range(1,8)) + list(range(9,13)):
    print(i, end = ' ')
print()

# 1 ~ 8, 9 ~ 13의 리스트를 생성한 후 i 출력