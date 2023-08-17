# *을 n개 출력하되 w마다 줄바꿈하기

print('*을 출력합니다.')
n = int(input('몇 개를 출력할까요?')) # 별 출력
w = int(input('몇 개마다 줄바꿈 할까요?')) # 줄 바꿈

for _ in range(n // w):
    print('*' * w) 
    
    '''
    *을  n//w번 반복하며 출력
    print는 자동으로 개행을 주기 때문에 줄바꿈 개수만큼 출력 후 줄바꿈
    '''

rest = n % w

if rest:
    print('*' * rest)

    '''
    마지막 행 출력 -> rest의 수만큼
    '''