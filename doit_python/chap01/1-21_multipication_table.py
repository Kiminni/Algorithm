# 구구단 곱셈표 출력하기
print('-' * 27)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end = '') # i가 1일 때 1 * j를 3자리로 가지런히 출력하기 위한 옵션 
    print()
print('-' * 27)