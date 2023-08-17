# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요: '))

for i in range(1, area + 1):
    if i * i > area : break # i가 가장 긴 변의 넓이 -> area보다 크면 종료
    if area % i : continue # 나머지 != 0 -> 처음으로(약수가 안되니)
    print(f'{i} * {area // i}')