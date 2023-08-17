# 왼쪽 아래가 직각인 이등변 삼각형을 *로 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.'))

for i in range(n):
    for j in range(i + 1):
        print('*', end = '') # i가 3일 때 0~2까지 증가시키면서 *을 출력 후 줄바꿈
    print()
