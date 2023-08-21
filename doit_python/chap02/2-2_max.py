# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any: 
    # 시퀀스형 a 원소의 최댓값 반환
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum :
            maximum = a[i]
    return maximum


# Any -> 제약이 없는 임의의 자료형, Sequence -> 시퀀스형(list, bytearry, str, tuple, bytes)
# input: Sequence, return: Any
'''
a의 원솟값 변경 x
함수를 호출 시 시퀀스 형태면 다 가능
int형이면 int 반환, float이면 float 반환
'''

if __name__ == '__main__': 
    print('배열의 최댓값을 구합니다.')
    num = int(input("원소의 개수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))
    
    print(f'최댓값은 {max_of(x)} 입니다.')


# 하나의 스크립트 프로그램 -> 모듈(여기선 2-2_max.py가 이름이니 얘가 모듈(.py를 포함하지 않는 파일의 이름 자체))
# if __name__ == '__main__': -> name과 main의 이름이 동일한지 확인
# 스크립트 프로그램 직접 실행 시 __name__ = __main__
# 임포트 될 때  __name__ = 그 모듈 이름(ex: max.py)
# 즉 여기서 max.py를 실행하지 않으면 14~21행은 실행 불가. 