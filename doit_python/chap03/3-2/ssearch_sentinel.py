# 보초법으로 수정한 알고리즘

import copy
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 값이 같은 원소를 선형 검색'''
    seq = copy.deepcopy(a) # a를 복사
    a.append(key) # 보초 key를 추가
    
    
    i = 0

    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i 


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    key = int(input('겁색할 값을 입력하세요: '))

    idx = seq_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')