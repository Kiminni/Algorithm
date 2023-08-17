# 2자리 양수 입력받기(10~99)

print('2자리 양수를 입력하세요.')

while True:
    no = int(input("값을 입력하세요: "))
    if no >= 10 and no <= 99:
    # if not(no < 10 or no > 99): 드모르간의 법칙 사용 -> 논리곱을 논리합, 논리합을 논리곱으로 바꾼 후 전체를 부정
        break

print(f'입력받은 양수는 {no} 입니다.')
print('입력받은 양수는 ' + str(no) + ' 입니다.')