'''
파이썬에서는 함수, 클래스 등을 모두 객체로 취급 -> 자료형을 갖고 메모리를 차지 -> 변수는 값을 갖지 않는다.
즉, 다른 변수와는 달리 변수가 값을 저장하는 상자같은 취급이 아님.

변수 = 객체를 참조하는 객체에 연결된 이름
모든 객체는 메모리를 차지, 자료형  + 식별 번호를 갖는다.

'''

n = 17
print(id(n)) # n의 식별 번호
print(id(17)) # 17의 식별 번호(n과 같음) 

'''
n에 17을 대입 후 id 함수를 2번 호출했는데, n = 17이 값을 복사하여 대입하지 않음.
-> 값 17의 int형 객체를 참조하는 n이라는 이름을 결합 -> 정수 리터럴 17과 n과의 식별 번호가 같다.
'''

'''
상자라고 생각한다면 17이라는 int형 객체 자체가 상자고, 변수는 값을 저장하는 상자가 아닌 이름임.
-> n을 17이 아닌 다른 수로 갱신한다면 그 수를 갖는 새로운 객체가 생성되고 n은 그걸 참조함.
'''


'''
파이썬의 변수는 객체의 식별 번호를 갖고오는 놈 -> 그냥 원래 있는 친구의 식별번호가 있어. 그 식별번호의 이름을 n이라고 정하는거지.
'''