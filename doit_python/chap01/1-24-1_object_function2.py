n = 1 # 전역 변수
def put_id():
    x = 1 # 지역 변수
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')

put_id()
          
# 모두가 int형 객체 1의 id 값을 가짐. 즉, n,x 얘네는 모두 그냥 int 객체 1의 다른 이름임.
# 파이썬에서는 함수의 시작과 종료가 객체 생성 소멸과 관련이 없음. -> for 1 ~ 100 반복 시 100개의 객체가 생성.

