# 오른쪽 아래가 직각인 이등변 삼각형을 *로 출력하기

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.'))

for i in range(n):
    for _ in range(n - i - 1): # 공백을 표현하기 위한 for 
        print(' ', end = '')
    for _ in range(i + 1): # *을 출력하기 위한 for
        print('*', end = '')
    print()

#  모든 행에서 공백과 *의 개수를 합치면 n 